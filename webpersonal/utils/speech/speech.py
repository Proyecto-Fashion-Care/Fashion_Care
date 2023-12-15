from gtts import gTTS
import speech_recognition as sr
import os

def speak(text):
    tts = gTTS(text=text, lang='es')
    tts.save("salida.mp3")
    os.system("afplay salida.mp3")
    os.remove("salida.mp3")


def listen():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Escuchando...")
        r.pause_threshold = 1
        r.energy_threshold = 200
        try:
            audio = r.listen(source, timeout=1)
            print("Procesando")
            text = r.recognize_google(audio, language="es-ES")
            print("Dijiste: {}".format(text))
            return text
        except:
            print("No te he entendido")
    

audio = listen()
speak(audio)
