# SpeechTextTranscriptionSeal
# Offline Speech-to-Text (Whisper)

A lightweight offline speech-to-text application built with Python and Faster-Whisper.

This project records audio directly from your microphone, transcribes it locally using OpenAI's Whisper model (via Faster-Whisper), and prints the transcription to the terminal.

No internet connection is required after the model has been downloaded.

---

## Features

- 🎤 Records directly from your microphone
- 🧠 Runs Whisper completely offline
- ⚡ Uses Faster-Whisper for fast transcription
- 🌍 Automatically detects spoken language
- 📝 Outputs clean text to the terminal
- 🔒 No cloud services or APIs required

---

## Example

```
Loading Whisper model...

Speak now...

Transcribing...

Detected language: en

You said:

Hello! This is a test of my offline speech-to-text system.
```

---

## Requirements

- Python 3.10+
- Microphone
- Windows, Linux or macOS

---

## Installation

Clone the repository:

```bash
git clone https://thabang-malele/SpeechTextTranscriptionSeal.git
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

### Windows

```powershell
.venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## Running

Simply execute:

```bash
python stt.py
```

The program will:

1. Load the Whisper model
2. Record audio from your microphone
3. Save it as `recording.wav`
4. Transcribe it
5. Print the detected language and transcription

---

## Configuration

Inside `stt.py` you can easily modify:

```python
SECONDS = 30
```

Length of the recording.

```python
SAMPLE_RATE = 16000
```

Recording sample rate.

```python
model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)
```

You can swap `"base"` for:

- `tiny`
- `base`
- `small`
- `medium`
- `large-v3`

Larger models are slower but generally produce more accurate transcriptions.

---

## Future Improvements

- Live streaming transcription
- GPU acceleration (CUDA / Vulkan / ROCm)
- Voice activity detection
- Automatic punctuation
- Speaker identification
- Save transcriptions to text files
- Llama.cpp integration
- Kokoro Text-to-Speech integration
- Fully offline AI voice assistant

---

## Technologies

- Python
- Faster-Whisper
- CTranslate2
- SoundDevice
- SciPy

---

## Why I Built This

I originally created this project while recovering from shoulder surgery. Typing for long periods was uncomfortable, so I wanted a simple offline way to speak naturally and have my computer transcribe what I said.

It also became the first building block toward a fully local AI assistant using:

- Whisper (Speech-to-Text)
- Llama.cpp (Language Model)
- Kokoro (Text-to-Speech)

---

## License

MIT License
