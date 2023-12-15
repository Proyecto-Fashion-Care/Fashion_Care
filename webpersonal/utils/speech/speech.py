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
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = r.listen(source)
        try:
            print("Procesando")
            text = r.recognize_google(audio, language="es-ES")
            print("Dijiste: {}".format(text))
        except:
            print("No te he entendido")
    return text

audio = listen()
speak(audio)
