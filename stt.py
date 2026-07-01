import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel

AUDIO_FILE = "recording.wav"
SECONDS = 10
SAMPLE_RATE = 16000

print("Loading Whisper model...")

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

print("Speak now...")

audio = sd.rec(
    int(SECONDS * SAMPLE_RATE),
    samplerate=SAMPLE_RATE,
    channels=1,
    dtype="int16"
)

sd.wait()
write(AUDIO_FILE, SAMPLE_RATE, audio)

print("Transcribing...")

segments, info = model.transcribe(AUDIO_FILE)

print(f"\nDetected language: {info.language}")
print("\nYou said:")

for segment in segments:
    print(segment.text)