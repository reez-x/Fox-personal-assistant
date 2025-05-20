from visuals import get_fox_panel
from command_parser import parse_command
from executor import execute_command
from rich.live import Live
from time import sleep
import speech_recognition as sr
from vosk_recognizer import listen_to_voice_vosk

# Versi listen yang tidak menggunakan print()
def listen_to_voice_vosk(live, status_text="🦊 Listening...") -> str:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        live.update(get_fox_panel(status_text))
        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            live.update(get_fox_panel("🦊 Timeout. No speech detected."))
            sleep(1)
            return ""

    try:
        text = r.recognize_google(audio)
        live.update(get_fox_panel(f"🦊 Heard: '{text}'"))
        return text
    except sr.UnknownValueError:
        live.update(get_fox_panel("🦊 I couldn't understand."))
        sleep(1)
        return ""
    except sr.RequestError:
        live.update(get_fox_panel("🦊 Voice service down."))
        sleep(1)
        return ""



def wait_for_wake_word(live):
    # Wake words (dalam bentuk full sentence, tidak terpisah lagi)
    wake_phrases = [
        "hello foxie", "hi foxie", "yo foxie",
        "hello foxy", "hi foxy", "yo foxy",
        "hello foksy", "hi foksy", "yo foksy",
        "hello voxie", "hi voxie", "yo voxie",
    ]

    while True:
        live.update(get_fox_panel("🦊 Say: 'Hello Foxie', 'Hi Foxie', or 'Yo Foxie'"))
        text = listen_to_voice_vosk(live, "🦊 Listening for wake word...")

        if text:
            text = text.lower()
            live.update(get_fox_panel(f"🦊 Heard: '{text}'"))  # Debugging output
            if any(wake in text for wake in wake_phrases):
                live.update(get_fox_panel("🦊 Wake word detected. I'm listening..."))
                return
            else:
                live.update(get_fox_panel(f"🦊 No wake word detected in: '{text}'"))
                sleep(1)


def main():
    with Live(get_fox_panel("🦊 Booting up..."), refresh_per_second=4) as live:
        sleep(1)
        while True:
            wait_for_wake_word(live)
            command = listen_to_voice_vosk(live, "🦊 Listening for command...")
            if command:
                live.update(get_fox_panel(f"🦊 You said: {command}"))
                action = parse_command(command)
                execute_command(action)
                sleep(1)

if __name__ == "__main__":
    main()
