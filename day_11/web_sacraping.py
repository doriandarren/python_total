import bs4
import requests

'''

Importante: utilice la página del instructor para pruebas
También existe una para hacer pruebas se llama: https://toscrape.com/

'''


## Ejemplo enlace: https://escueladirecta-blog.blogspot.com/


##resultado = requests.get('https://www.amazon.es/WEIBIDA-Plataforma-Acolchadas-Frigor%C3%ADfico-Electrodom%C3%A9sticos/dp/B0BN7XN3KW/?_encoding=UTF8&pd_rd_w=bfRUi&content-id=amzn1.sym.8e0b9c93-ce4d-43a7-92b8-93ac944c3311%3Aamzn1.symc.fc11ad14-99c1-406b-aa77-051d0ba1aade&pf_rd_p=8e0b9c93-ce4d-43a7-92b8-93ac944c3311&pf_rd_r=MB3PJVFZ52WDRGRRM798&pd_rd_wg=bAsaI&pd_rd_r=f33e7197-a65b-42a8-a66a-e699bce137fc&ref_=pd_hp_d_atf_ci_mcx_mr_ca_hp_atf_d')
resultado = requests.get('https://escueladirecta-blog.blogspot.com/')

##print(type(resultado))
## print(resultado.text)

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

## print(sopa.select('title'))
##print(sopa.select('title')[0].getText())



## Descargar Imagen:
#imagenes = sopa.select('img')[0]['src']

#for i in imagenes:
#    print(i)


imagenes = sopa.select('img')[0]['src']
imagen_1 = requests.get(imagenes)
## print(imagen_1.content)

f = open('mi_imagen_webscrapping.jpg', 'wb')
f.write(imagen_1.content)
f.close()










