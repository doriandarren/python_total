import pyautogui
import time

def capture_screen_region(region, output_file="screenshot_region.png", interval=1):
    """
    Captura un fragmento específico de la pantalla cada cierto intervalo.
    :param region: Tupla con las coordenadas y dimensiones (x, y, width, height).
    :param output_file: Nombre base del archivo donde se guardarán las capturas.
    :param interval: Intervalo en segundos entre capturas.
    """
    counter = 0
    print(f"Iniciando capturas cada {interval} segundo(s). Presiona Ctrl+C para detener.")
    try:
        while True:
            # Capturar la región de la pantalla
            screenshot = pyautogui.screenshot(region=region)
            # Guardar la captura en un archivo
            file_name = f"{output_file}_{counter}.png"
            screenshot.save(file_name)
            print(f"Captura guardada: {file_name}")
            counter += 1
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Capturas detenidas por el usuario.")
    except Exception as e:
        print(f"Error durante la captura: {e}")

if __name__ == "__main__":
    # Define el área a capturar (x, y, ancho, alto)
    region = (100, 100, 400, 300)  # Ajusta el área según tu necesidad
    capture_screen_region(region, output_file="captura", interval=1)