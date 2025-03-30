from asistente_virtual.helpers.helper_api import http_get
from asistente_virtual.helpers.spinner import Spinner
from asistente_virtual.helpers.speak import speak


def query(prompt):

    spinner = Spinner("Enviando datos al modelo...")
    spinner.start()

    data = http_get(prompt)

    spinner.stop()

    if data:
        ## print("Datos obtenidos:", data)

        resp_text = data["choices"][0]["text"].strip()

        speak(resp_text)

        print("Respuesta del modelo:", resp_text)


    else:
        print("No se pudieron obtener datos.")