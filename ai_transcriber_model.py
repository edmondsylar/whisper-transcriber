import whisper
import os

def transcribe_audio(audio):
    model = whisper.load_model("base")
    result = model.transcribe(audio)

    # return transcription
    return result

# def clean_data and write to txt
def clean_data(data, name):
    with open(f"{name}.txt", "w") as f:
        f.write(data)