from vosk import Model, KaldiRecognizer
import sounddevice as sd
import queue
import json
import pyttsx3



# Cargar el modelo de Vosk
model_path = "vosk-model-small-es-0.42"  # Ruta al modelo de idioma (descargado previamente)
model = Model(model_path)

# Configuración del micrófono
SAMPLE_RATE = 16000  # Frecuencia de muestreo
CHANNELS = 1  # Número de canales (mono)


# Configuración de pyttsx3
engine = pyttsx3.init()

#last_transcription = ""  # Variable para guardar la última transcripción


# Cola para almacenar datos de audio
q = queue.Queue()

def say(msg):
    """Función para sintetizar texto a voz."""
    print(f"Diciendo: {msg}")
    engine.say(msg)
    engine.runAndWait()



# Función para capturar audio en la cola
def audio_callback(indata, frames, time, status):
    if status:
        print(status)  # Imprime cualquier advertencia o error del micrófono
    q.put(bytes(indata))



# Inicializa el flujo de grabación y reconocimiento
def main():

    # global last_transcription  # Usar la variable global para almacenar la última transcripción

    print("Iniciando grabación. Habla algo...")
    recognizer = KaldiRecognizer(model, SAMPLE_RATE)

    with sd.RawInputStream(samplerate=SAMPLE_RATE, blocksize=8000, dtype="int16",
                           channels=CHANNELS, callback=audio_callback):
        try:
            while True:
                # Obtiene datos de la cola
                data = q.get()
                if recognizer.AcceptWaveform(data):
                    # Transcripción completa
                    result = json.loads(recognizer.Result())

                    r = result.get("text", "")
                    print("Texto reconocido:", r)

                    # Evitar repetición de la misma palabra o frase
                    # if r and r != last_transcription:
                    #     print("Texto reconocido:", r)
                    #     say(r)
                    #     last_transcription = r  # Actualiza la última transcrip

                else:
                    # Resultado parcial (opcional)
                    partial_result = json.loads(recognizer.PartialResult())
                    print("Texto parcial:", partial_result.get("partial", ""))
        except KeyboardInterrupt:
            print("\nGrabación detenida.")
        except Exception as e:
            print("Error:", str(e))






# Llamar a la función principal
if __name__ == "__main__":

    main()
