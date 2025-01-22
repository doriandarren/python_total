import pyautogui
import pytesseract
import re
import time


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
            print(f"Números encontrados: {numbers}")

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


if __name__ == "__main__":
    # Define el área de captura (x, y, ancho, alto)
    region = (100, 100, 400, 300)  # Ajusta el área según tu necesidad
    capture_and_process(region, interval=2)
