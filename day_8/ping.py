# import os
#
# def check_server(hostname):
#     response = os.system(f"ping -c 1 {hostname}")
#
#     if response == 0:
#         print(f"{hostname} está activo.")
#     else:
#         print(f"{hostname} no responde.")
#
#
#
# check_server("www.google.com")


import psutil
import time

def monitorizar_servidor_y_guardar():
    while True:
        # Obtener métricas
        cpu = psutil.cpu_percent(interval=1)
        memoria = psutil.virtual_memory()

        # Crear un mensaje de monitoreo
        mensaje = f"CPU: {cpu}% | Memoria usada: {memoria.percent}%\n"

        # Guardar en un archivo
        with open("monitoreo_servidor.log", "a") as archivo:
            archivo.write(mensaje)

        # Mostrar el mensaje en la consola (opcional)
        print(mensaje.strip())

        # Esperar 60 segundos antes de la próxima ejecución
        time.sleep(60)

monitorizar_servidor_y_guardar()