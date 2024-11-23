import http.client
import json

conn = http.client.HTTPSConnection("spotify23.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "22d14176b7msh826935d3801a7ffp1d2838jsnbe0087661902",
    'x-rapidapi-host': "spotify23.p.rapidapi.com"
}

conn.request("GET", "/search/?q=q%3Dtaylor%2Bswift&type=multi&offset=0&limit=10&numberOfTopResults=5", headers=headers)

res = conn.getresponse()
data = res.read().decode("utf-8")
data_dict = json.loads(data)

print(json.dumps(data_dict, indent=4))
#print(data_dict)

# Accediendo correctamente a los álbumes
if 'albums' in data_dict:
    albums = data_dict['albums']
    if 'items' in albums:
        for item in albums['items']:
            print(item['data'])  # Puedes personalizar el contenido que imprimes aquí
else:
    print("No se encontraron álbumes en la respuesta.")