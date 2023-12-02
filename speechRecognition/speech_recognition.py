import speech_recognition as sr
import pyttsx3
import time
import threading

def getAudio():
    """
    Función que captura el audio a través de un micrófono.
    Devuelve un texto: str
    """

    #Creamos la instancia del reconocedor y del micrófono
    r = sr.Recognizer()
    mic = sr.Microphone()

    while True:
        with mic as source:
            print("Escuchando...")
            r.pause_threshold = 2
            r.adjust_for_ambient_noise(source)

            try:
                audio = r.listen(source, timeoff=1)
                print("Procesando...")
                text = r.recognize_google(audio, language="es-ES")
                return text
            except sr.UnknownValueError:
                print("No he entendido lo que has dicho, por favor repítelo.")
            except sr.RequestError as e:
                print("Error en la solicitud: {e}".format(e))
            except sr.WaitTimeoutError:
                print("Time out.")

def writeText(text):
    """
    Función para escribir texto
    """
    for char in text:
        print(char, end="")
        time.sleep(0.07)

def speakText(text):
    """
    Función que reproduce como audio el texto introducido
    """
    engine = pyttsx3.init()
    engine.setProperty("rate", 125) #Ajustamos la velocidad de lectura
    engine.say(text)
    engine.runAndWait()
    


            


