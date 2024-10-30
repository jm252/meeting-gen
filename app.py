# app.py

from flask import Flask, render_template, request, redirect, url_for, flash, send_file
import os
import cv2

from files import convert_to_mp3
from transcribe_audio import transcribe_audio
from image_to_text import get_text_on_screen, get_screen_image
from transcript_utils import is_junk_text, is_similar

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'supersecretkey'

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Check if a file is part of the request
    if 'file' not in request.files:
        flash('No file part in the request')
        return redirect(url_for('index'))

    file = request.files['file']

    if file.filename == '':
        flash('No file selected')
        return redirect(url_for('index'))

    if file and file.filename.endswith('.mp4'):
        # Save the uploaded file
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        audio_path = convert_to_mp3(file_path)
        print("TRANSCRIBING")
        transcript_segments = transcribe_audio(audio_path)

        record = ''
        section_text = ''
        text_segments = []
        image_paths = []
        image_list = []

        for segment in transcript_segments:
            if record == '':
                record += "Speaker: " + segment.text
                section_text += "Speaker: " + segment.text
                continue

            start = segment.start

            if record[-1] in ['.', '?', '!']:
                record += '\n\n'
                section_text += '\n\n'
                
                # Capture the current screen as an image
                screen_image = get_screen_image(file_path, start)

                # Check if the image is similar to previously appended images
                if screen_image is not None and not is_similar(screen_image, image_list):
                    image_list.append(screen_image)  # Add new unique screen image to the list
                    text_on_screen = get_text_on_screen(screen_image)  # Get text from the unique image
                    
                    # Save image to static folder for display
                    image_filename = f"screen_{int(start)}.png"
                    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)
                    cv2.imwrite(image_path, screen_image)
                    image_paths.append(f"uploads/{image_filename}")  # Store the image path for the HTML display
                    
                    # Add the transcript and screen text for the downloadable text record
                    if not is_junk_text(text_on_screen):
                        text_segments.append(section_text)
                        section_text = ''
                        record += '=' * 50 + '\n'
                        record += "The screen now reads:\n" + text_on_screen + '\n' + '=' * 50
                        record += '\n\n' + "Speaker: "
                    else:
                        print("Skipping junk text")
            else:
                print("No processing, just appending")

            record += segment.text
            section_text += segment.text

        # Final output for the downloadable record
        transcript_path = os.path.join(app.config['UPLOAD_FOLDER'], 'transcript.txt')
        with open(transcript_path, 'w') as f:
            f.write(record)

        # Prepare data to pass to the template
        transcript_data = [{"text": text, "image": image} for text, image in zip(text_segments, image_paths)]

        # Render template with the data
        return render_template('generate.html', transcript_data=transcript_data)

    else:
        flash('Invalid file type. Only MP4 files are allowed.')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
