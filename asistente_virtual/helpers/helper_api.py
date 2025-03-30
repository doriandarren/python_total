import requests


def http_get(prompt):
    url = "http://192.168.1.100:11434/v1/completions"  # IP local, asegúrate de que esté accesible

    payload = {
        "model": "deepseek-v2",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Si no es 2xx, lanza excepción
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud HTTP: {e}")
        return None

