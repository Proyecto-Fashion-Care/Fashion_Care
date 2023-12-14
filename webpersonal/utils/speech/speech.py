from gtts import gTTS
import os

def speak(text):
    tts = gTTS(text=text, lang='es')
    tts.save("salida.mp3")
    os.system("afplay salida.mp3")
    os.remove("salida.mp3")



