import sounddevice as sd
from scipy.io.wavfile import write

seconds = 5
sample_rate = 16000

print("Speak now...")

audio = sd.rec(
    int(seconds * sample_rate),
    samplerate=sample_rate,
    channels=1,
    dtype="int16"
)

sd.wait()

write("recording.wav", sample_rate, audio)

print("Saved as recording.wav")