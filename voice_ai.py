import speech_recognition as sr
import threading

voice_command = ""
voice_active = False

def listen():
    global voice_command, voice_active

    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        while True:
            try:
                audio = r.listen(source, timeout=2, phrase_time_limit=4)
                text = r.recognize_google(audio).lower()
                print("Voice:", text)

                if "hey mic" in text:
                    voice_active = True

                elif "stop" in text:
                    voice_active = False

                elif voice_active:
                    voice_command = text

            except:
                pass

def start_voice():
    threading.Thread(target=listen, daemon=True).start()