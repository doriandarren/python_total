from pathlib import Path

base = Path.home()
guia = Path(base, "Europa", "España", Path("Barcelona", "Sagrada_Familia.txt"))

guia2 = guia.with_name("La_Pedrera.txt")

# print(base)
# print(guia)
# print(guia2)

## Niveles
print(guia.parents[3])


print(Path(Path.home(), "Europa"))

guia3 = Path(Path.home(), "Europa")

## Listar todos:  for txt in Path(guia3).glob("*.txt"):
#for txt in Path(guia3).glob("**/*.txt"): ## Recursivo
    #print(txt)



guia4 = Path("Europa", "España", "Barcelona", "Sagrada_Familia.txt")
en_europa = guia4.relative_to(Path("Europa"))

en_espania = guia4.relative_to(Path("Europa", "España"))

print(en_europa)
print(en_espania)
