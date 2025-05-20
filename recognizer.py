# recognizer.py
import speech_recognition as sr

def listen_to_voice_vosk():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🦊 Listening...")
        audio = r.listen(source)
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print("❌ Fox couldn't understand.")
    except sr.RequestError:
        print("⚠️ No internet connection.")
    return None
