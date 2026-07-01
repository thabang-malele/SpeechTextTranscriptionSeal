from faster_whisper import WhisperModel

print("Loading model...")

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

print("Transcribing...")

segments, info = model.transcribe("recording.wav")

print(f"\nDetected language: {info.language}")

print("\nYou said:")

for segment in segments:
    print(segment.text)