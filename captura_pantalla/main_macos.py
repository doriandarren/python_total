from PIL import ImageGrab
import pytesseract
import re
import os
import time
from db_connection import insert_data



# Configuración para macOS
# Configura la ruta de Tesseract si es necesario
# pytesseract.pytesseract.tesseract_cmd = "/usr/local/bin/tesseract"

## Para Macos
def capture_and_extract(capture_area, temp_image="captura_area.png"):
    """
    Captura un área específica de la pantalla, extrae números y elimina la imagen.
    :param capture_area: Tupla con las coordenadas del área a capturar (x1, y1, x2, y2)
    :param temp_image: Nombre del archivo temporal para guardar la captura
    :return: Texto extraído y lista de números encontrados
    """
    try:
        # Capturar la pantalla en el área definida
        screenshot = ImageGrab.grab(bbox=capture_area)

        # Guardar la captura temporalmente
        screenshot.save(temp_image)

        # Extraer texto de la imagen usando Tesseract
        text = pytesseract.image_to_string(screenshot)

        # Buscar números con formato específico (comas y puntos)
        pattern = r'\b\d{1,3}(?:,\d{3})+\.\d+\b'
        numbers = re.findall(pattern, text)

        # Buscar valores con signos (+ o -)
        pattern_signs = r'[+-]\d+\.\d+'
        signed_numbers = re.findall(pattern_signs, text)

        # Mostrar los resultados
        print("Texto extraído:", text)
        print("Números encontrados:", numbers)
        print("Valores con signo encontrados:", signed_numbers)



        # Eliminar la imagen temporal
        # if os.path.exists(temp_image):
        #     os.remove(temp_image)
        #     print(f"Imagen temporal '{temp_image}' eliminada.")

        return text, numbers

    except Exception as e:
        print(f"Error durante la captura y extracción: {e}")
        return None, None


## Para YahooFinance
def capture_and_extract2(capture_area, temp_image="captura_area.png"):
    """
    Captura un área específica de la pantalla, extrae números específicos y elimina la imagen.
    :param capture_area: Tupla con las coordenadas del área a capturar (x1, y1, x2, y2)
    :param temp_image: Nombre del archivo temporal para guardar la captura
    :return: Texto extraído y lista de números encontrados
    """
    try:
        # Capturar la pantalla en el área definida
        screenshot = ImageGrab.grab(bbox=capture_area)

        # Guardar la captura temporalmente
        screenshot.save(temp_image)

        # Extraer texto de la imagen usando Tesseract
        text = pytesseract.image_to_string(screenshot)





        # Buscar números con formato específico (signo opcional, punto como separador de miles y coma como decimal)
        pattern = r'[+-]?\d{1,3}(?:\.\d{3})*,\d{2}'
        all_numbers = re.findall(pattern, text)

        # Mostrar los resultados
        print("Texto extraído:", text)
        print("Números encontrados:", all_numbers)

        # Eliminar la imagen temporal
        # if os.path.exists(temp_image):
        #     os.remove(temp_image)
        #     print(f"Imagen temporal '{temp_image}' eliminada.")

        return text, all_numbers

    except Exception as e:
        print(f"Error durante la captura y extracción: {e}")
        return None, None






def loadWhile():
    """
    Método principal para ejecutar la captura periódicamente cada minuto.
    """
    # Define el área de captura (ajusta según tu pantalla)
    ## capture_area = (500, 250, 980, 300)  ## No borrara es para la macos del curro
    ##capture_area = (250, 300, 900, 400)  ## YahooFinance

    capture_area = (500, 250, 780, 300)

    # Ejecutar periódicamente cada minuto
    print("Iniciando cron para capturar cada minuto... Presiona Ctrl+C para detener.")
    try:
        while True:
            ##capture_and_extract(capture_area)
            capture_and_extract2(capture_area)
            time.sleep(5)  # 60 = Esperar 1 minuto
    except KeyboardInterrupt:
        print("Cron detenido por el usuario.")









if __name__ == "__main__":

    loadWhile()

    ## Funciona pero tengo que integrarlo con lo que va vaya hacer con los datos
    # numbers = ['96,439.4']  # Ejemplo
    # signed_numbers = ['+1.32', '-0.85']  # Ejemplo
    # insert_data(numbers, signed_numbers)




