import whisper

model = whisper.load_model("base")

def transcribe(recording):
    # pass transcription
    result = model.transcribe(f"{recording}")
    print(result["text"])
    return result

# call the function
transcribe("coca-cola.m4a")