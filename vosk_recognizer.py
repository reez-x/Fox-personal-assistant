from vosk import Model, KaldiRecognizer
import sounddevice as sd
import json
from visuals import get_fox_panel
from rich.live import Live

# Inisialisasi model Vosk
model = Model("vosk-model-small-en-us-0.15")  # Sesuaikan path jika berbeda

def listen_to_voice_vosk(live: Live, prompt="🦊 Listening...") -> str:
    samplerate = 16000
    duration = 5  # max duration to listen
    rec = KaldiRecognizer(model, samplerate)

    live.update(get_fox_panel(prompt))
    print("🎙️ Vosk: Listening...")

    try:
        recording = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype='int16')
        sd.wait()  # Tunggu sampai rekaman selesai
        frames = recording.tobytes()

        if rec.AcceptWaveform(frames):
            result = json.loads(rec.Result())
            text = result.get("text", "")
            live.update(get_fox_panel(f"🦊 Heard (Vosk): '{text}'"))
            return text
        else:
            partial = json.loads(rec.PartialResult()).get("partial", "")
            live.update(get_fox_panel(f"🦊 Heard (partial): '{partial}'"))
            return partial

    except Exception as e:
        live.update(get_fox_panel(f"🦊 Error: {str(e)}"))
        return ""
