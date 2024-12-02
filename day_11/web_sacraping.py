import bs4
import requests



## Ejemplo enlace: https://escueladirecta-blog.blogspot.com/

resultado = requests.get('https://escueladirecta-blog.blogspot.com/')

print(type(resultado))

print(resultado.text)

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

print(sopa)



