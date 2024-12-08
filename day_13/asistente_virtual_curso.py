import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia



def trasfromar_audio_en_texto():

    #variable
    r = sr.Recognizer()

    with sr.Microphone() as origen:

        # tiempo de espera
        r.pause_threshold = 0.8

        print("Ya puedes hablar")

        audio = r.listen(origen)

        # try:
        #     pedido = r.recognize_google(audio, language="es-es")
        #
        #     # prubea de que puedo ingresar
        #     print("Dijiste: " + pedido)




## Funcion para que se escuche
def hablar(mensaje):

    engine = pyttsx3.init()

    engine.say(mensaje)
    engine.runAndWait()



hablar("Hola mundo")
