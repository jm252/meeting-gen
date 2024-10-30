import os

from pydub import AudioSegment
from constants import SECONDS_TO_PROCESS
from openai_client import CLIENT

def transcribe_audio(audio_path):
    """ Transcribes the audio using OpenAI Whisper API.

    Args:
      audio_path: The path to the audio file.

    Returns:
      The transcription segments of the audio.

    """
    segment = AudioSegment.from_mp3(audio_path)
    processed_audio_path = "processed" + audio_path

    # PyDub handles time in milliseconds
    if SECONDS_TO_PROCESS is not None:
        # Calculate time in milliseconds and define the new file path
        num_seconds = SECONDS_TO_PROCESS * 1000
        first_seconds = segment[:num_seconds]
        processed_audio_path = f"{os.path.splitext(audio_path)[0]}_FIRST_{SECONDS_TO_PROCESS}_SECONDS.mp3"
        # Export only the first segment
        first_seconds.export(processed_audio_path, format="mp3")
    else:
      segment.export(processed_audio_path, format="mp3")

    # Open the audio file in binary mode
    with open(processed_audio_path, "rb") as audio_file:
        # Call the OpenAI Whisper API to transcribe the audio
        transcription = CLIENT.audio.transcriptions.create(
            model="whisper",
            file=audio_file,
            response_format="verbose_json",
            timestamp_granularities=["segment"]
        )
    return transcription.segments