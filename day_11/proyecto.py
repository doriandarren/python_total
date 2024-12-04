import bs4
import requests


## https://books.toscrape.com/catalogue/page-3.html

url_base = 'https://books.toscrape.com/catalogue/page-{}.html'
##print(url_base.format('2'))


#Lista de titulos co 4 o 5 estrellas
titulos_ranting_alto = []


#iterar páginas

for pagina in range(1, 51):

    #crear pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    # seleecionar datos de los libros
    libros = sopa.select('.product_pod')

    for libro in libros:

        # 4 -5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:

            #guardar titulo libro
            titulo_libro = libro.select('a')[1]['title']

            titulos_ranting_alto.append(titulo_libro)


## ver libro 4 -5 estrelllas en consola
for t in titulos_ranting_alto:
    print(t)

