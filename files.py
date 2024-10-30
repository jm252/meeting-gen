import os
from moviepy.editor import VideoFileClip


def convert_to_mp3(video_path) -> str:
    """ Converts a video file to an mp3 file.

    Args:
      video_path: The path to the video file.

    Returns:
      The path to the mp3 file.

    """
    # Extract audio from video and convert to MP3
    video = VideoFileClip(video_path)
    audio_path = f"{os.path.splitext(video_path)[0]}.mp3"
    if os.path.exists(audio_path):
        return audio_path
    video.audio.write_audiofile(audio_path, codec='mp3')
    return audio_path

def save_transcript_to_file(transcript, file_name="record.txt") -> None:
    """
    Saves the given transcript to a file.

    Args:
        transcript (str): The transcript to be saved.
        file_name (str): The name of the file to save the transcript to.
    """
    with open(file_name, "w") as file:
        file.write(transcript)