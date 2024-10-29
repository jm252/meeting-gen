from flask import Flask, render_template, request, redirect, url_for, flash, send_file
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'supersecretkey'

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

        # Generate a placeholder transcript
        # TODO: call actually function to generate and return transcrpt file
        transcript_content = f'This is a placeholder transcript for {file.filename}.'
        transcript_path = os.path.join(app.config['UPLOAD_FOLDER'], 'transcript.txt')
        with open(transcript_path, 'w') as f:
            f.write(transcript_content)

        # Render the generate.html page with the download link
        return render_template('generate.html', transcript_path=transcript_path)
    else:
        flash('Invalid file type. Only MP4 files are allowed.')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
