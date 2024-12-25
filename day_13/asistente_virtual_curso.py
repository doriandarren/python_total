import pyttsx3
##import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
from vosk import Model, KaldiRecognizer
import sounddevice as sd
import queue

from day_11.proyecto import resultado


def trasfromar_audio_en_texto():
    # Cargar el modelo de Vosk
    model = Model("vosk-model-small-es-0.42")  # Asegúrate de que este directorio contiene tu modelo de Vosk.
    recognizer = KaldiRecognizer(model, 16000)  # Frecuencia de muestreo a 16kHz

    # Cola para manejar los datos de audio en tiempo real
    audio_queue = queue.Queue()

    # Función callback para el micrófono
    def callback(indata, frames, time, status):
        if status:
            print(f"Estado del micrófono: {status}")
        audio_queue.put(bytes(indata))

    # Configurar el stream de audio
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("Di algo...")
        while True:
            data = audio_queue.get()
            if recognizer.AcceptWaveform(data):
                # Resultado como JSON
                result = recognizer.Result()
                text = eval(result)["text"]  # Extraer solo el texto
                print(f"Texto detectado: {text}")
                return text  # Salir después de detectar la primera frase
            else:
                partial_result = recognizer.PartialResult()
                print(f"Texto parcial: {eval(partial_result)['partial']}")  # Opcional para debug





## Funcion para que se escuche
def hablar(mensaje):

    engine = pyttsx3.init()

    engine.say(mensaje)
    engine.runAndWait()



def saludo_inicial():
    hora  = datetime.datetime.now()

    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif hora.hour >= 6 and hora.hour < 13:
        momento = 'Buenos días'
    else:
        momento = 'Buenas tardes'

    hablar(f'{momento}, soy Elena, tu asistente personal. Por favor, dime en que te puedo ayudar')





def pedir_cosas():

    saludo_inicial()

    comenzar = True

    while comenzar:

        pedido = trasfromar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar(f'Con gusto, estoy abriendo youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar(f'Claro, estoy en ello')
            webbrowser.open('https://www.google.com')
            continue
        # elif 'busca en wikipedia' in pedido:
        #     hablar('Buscando eso en wikipeadia')
        #     pedido = pedido.replace('busca en wikipeadia', '')
        #     wikipedia.set_lang('es')
        #     wikipedia.summary(pedido, sentences=1)
        #     hablar('Wikipedia dice lo siguiente: ')
        #     hablar(resultado)
        #     continue
        elif 'busca en internet' in pedido:
            hablar('Buscando eso en internet')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Es es lo que encontró: ')
            continue
        elif 'reproducir' in pedido:
            hablar('Nueba idea, ya comienzo a reproducirlo')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {
                'apple': 'APPL',
                'amazon': 'AMZN',
                'google': 'GOOGL',
            }

            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontré, el precio de {accion}  es {precio_actual}')
                continue
            except:
                hablar('Perdón pero no la encontrado')
                continue
        elif 'adiós' in pedido:
            hablar("Me voy a descansar, cualquier cosa me avisas")
            break




##texto_final = trasfromar_audio_en_texto()
##print(f'Texto final: {texto_final}')
##hablar(texto_final)

pedir_cosas()