import pyautogui
import pytesseract
import os
import re
import time

from sqlalchemy.sql.functions import count

from db_connection import insert_data


def capture_and_process(region, interval=1, output_file="screenshot_region.png"):
    """
    Captura un fragmento específico de la pantalla, extrae texto y procesa números.
    :param region: Tupla con las coordenadas y dimensiones (x, y, width, height).
    :param interval: Intervalo en segundos entre capturas.
    :param output_file: Nombre base del archivo donde se guardarán las capturas.
    """
    print(f"Iniciando capturas cada {interval} segundo(s). Presiona Ctrl+C para detener.")
    try:
        while True:
            # Capturar la región de la pantalla
            screenshot = pyautogui.screenshot(region=region)
            screenshot.save(output_file)

            # Extraer texto con pytesseract
            text = pytesseract.image_to_string(output_file)
            print(f"Texto extraído: {text}")

            # Procesar números
            numbers = extract_numbers(text)
            #print(f"Números encontrados: {numbers}")

            if len(numbers) > 0:
                fnumber = format_number(numbers[0])
                insert_data(fnumber, 0.0)


            # if len(numbers) > 2:
            #     fnumber = format_number(numbers[1])
            #
            #     print(f"{fnumber}")
            #     insert_data(fnumber, 0.0)


            # Eliminar el archivo de imagen después de procesarlo
            if os.path.exists(output_file):
                os.remove(output_file)

            # Pausar hasta la próxima captura
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Capturas detenidas por el usuario.")
    except Exception as e:
        print(f"Error: {e}")


def extract_numbers(text):
    """
    Extrae números del texto usando expresiones regulares.
    :param text: Texto extraído de la imagen.
    :return: Lista de números encontrados.
    """
    # Patrón para números (formato decimal y con signo opcional)
    pattern = r'[+-]?\d+(?:,\d{3})?(?:\.\d+)?'
    return re.findall(pattern, text)



def format_number(number):
    print(number)
    return number.replace(",", "")




if __name__ == "__main__":
    # Define el área de captura (x, y, ancho, alto)
    # region = (100, 100, 400, 300)  # Ajusta el área según tu necesidad
    region = (100, 120, 300, 100)  # Ajusta el área según tu necesidad
    capture_and_process(region, interval=2)

    # numbers = ['96,439.4']  # Ejemplo
    # signed_numbers = ['+1.32', '-0.85']  # Ejemplo
    # insert_data(numbers, signed_numbers)
