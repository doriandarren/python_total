import requests

# URL del webhook de Discord
url = 'https://discord.com/api/webhooks/1262688358493323324/k_UyCO24VXl2UxGEYOtdObFHb9a0lR7TJn2Gl_2OddSN1YM51CMB3dgVSLG-s5wpPm4z'

def send_message(content):
    """
        Envía un mensaje al webhook de Discord.

        Args:
            content (str): El contenido del mensaje a enviar.
        """
    data = {
        "content": content,  # El mensaje que quieres enviar
        "username": "PythonBot"  # Nombre que aparecerá en Discord
    }

    response = requests.post(url, json=data)

    if response.status_code == 204:
        print("Mensaje enviado exitosamente.")
    else:
        print(f"Error al enviar mensaje: {response.status_code} - {response.text}")





# Llamada a la función para enviar el mensaje
send_message("¡Hola desde Python! 🐍")