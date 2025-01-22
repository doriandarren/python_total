import pyautogui

def capture_screen(output_file="screenshot.png"):
    try:
        # Toma la captura de pantalla completa
        screenshot = pyautogui.screenshot()
        # Guarda la imagen en un archivo
        screenshot.save(output_file)
        print(f"Captura guardada en {output_file}")
    except Exception as e:
        print(f"Error al capturar la pantalla: {e}")

if __name__ == "__main__":
    capture_screen()