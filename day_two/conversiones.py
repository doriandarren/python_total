
## implicitas
num1 = 20
num2 = 30.5

num1 = num1 + num2

print(type(num1))
print(type(num2))


## Explicitas

num3 = 5.8
print(num3)
print(type(num3))

num4 = int(num3)
print(num4)
print(type(num4))


edad = input("Edad: ")
edad = int(edad)

nueva_edad = 1 + edad
print(f"Tu nueva edad {nueva_edad}")