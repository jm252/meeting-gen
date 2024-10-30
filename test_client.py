from openai import AzureOpenAI
from transcribe_audio import transcribe_audio
from pydub import AudioSegment
import os


CLIENT = AzureOpenAI(
    api_key="FUwFEsKnzCNeaB4l3xW3HpybYreDgrMkcp35LfSRBeYA0idPxOr7JQQJ99AJACHYHv6XJ3w3AAABACOG0FFq",
    api_version="2024-02-01",
    azure_endpoint="https://jg003-m2vyznzu-eastus2.openai.azure.com/openai/deployments/whisper/audio/translations?api-version=2024-06-01"
)


def transcribe_audio(audio_path):
    """ Transcribes the audio using OpenAI Whisper API.

    Args:
      audio_path: The path to the audio file.

    Returns:
      The transcription segments of the audio.

    """
    segment = AudioSegment.from_mp3(audio_path)
    processed_audio_path = "processed" + audio_path
    SECONDS_TO_PROCESS = 50
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

segments = transcribe_audio("static/uploads/COS217.mp3")
print(segments)