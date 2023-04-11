"""
#### 3.
Escribir un programa que almacene la cadena de caracteres <b>contraseña</b> en una variable, pregunte al usuario 
por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la 
variable sin tener en cuenta mayúsculas y minúsculas.
"""
print('''
FUNDAMENTOS DE PROGRAMACION
NOMBRE: Jhordan Pizango


Fecha: 30/03/2023

''')


password = "contraseña"
user_password = input("Ingrese Contraseña: ")

if password == user_password:
    print("Coincide")
else:
    print("Contraseña distinta")