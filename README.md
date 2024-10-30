# MeetingGen.AI

MeetingGen.AI is an AI-powered web application designed to transcribe meeting videos and extract on-screen text for a rich transcript experience. It allows users to upload an `.mp4` file, processes the video to create a time-stamped transcript, and displays both the spoken content and screenshots of the screen text in sequence. The transcript is also available for download as a text file.

## Features

- **Audio Transcription**: Uses OpenAI’s Whisper API to convert spoken audio into a text transcript.
- **Screen Text Extraction**: Captures on-screen text at key moments using OCR, displaying the exact screen image for context.
- **Intelligent Filtering**: Filters out repetitive or low-value screen content for a cleaner, more relevant transcript.
- **Downloadable Transcript**: Allows users to download the full text transcript of the meeting.

## Getting Started

Follow these instructions to set up and run MeetingGen.AI.

### Prerequisites

- **Python 3.7 or higher** installed on your system.
- **ffmpeg** for audio and video processing (instructions provided below).

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository_url>
   cd meeting-gen-ai
   ```

2. **Create and Activate a Virtual Environment**

   - **MacOS/Linux**
     ```bash
     python3 -m venv env
     source env/bin/activate
     ```

   - **Windows**
     ```bash
     python -m venv env
     .\env\Scripts\activate
     ```

3. **Install the Required Packages**

   After activating the virtual environment, install the dependencies from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Once the environment is set up, you can start the application with the following command:

```bash
python3 app.py
```

This will launch the Flask web server, and you can access the application by opening your web browser and navigating to `http://127.0.0.1:5000`.

### Troubleshooting `ffmpeg` Errors

If you encounter an error related to `ffmpeg`, it means the application is unable to find `ffmpeg`, which is required for processing audio and video files. Follow these steps to install it:

- **MacOS**: Install using Homebrew
  ```bash
  brew install ffmpeg
  ```

- **Ubuntu/Debian**: Install using `apt`
  ```bash
  sudo apt update
  sudo apt install ffmpeg
  ```

- **Windows**:
  1. Download `ffmpeg` from the [official website](https://ffmpeg.org/download.html).
  2. Extract the files, and add the `ffmpeg/bin` folder to your system’s PATH.
  3. Verify installation by running `ffmpeg -version` in Command Prompt.

After installing `ffmpeg`, re-run the application with:

```bash
python3 app.py
```

### Usage

1. Upload an `.mp4` video file through the provided interface.
2. Wait for the application to process the video and generate the transcript.
3. View the transcript with interleaved screen images or download the text-only transcript.

## Additional Notes

- The `.gitignore` includes `env/` and `static/uploads/` to prevent storing virtual environments and temporary image files in the repository.
- `requirements.txt` contains all necessary Python packages for running the application.