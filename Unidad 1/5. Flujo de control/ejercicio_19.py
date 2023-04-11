"""
19. Escribir un programa que pida al usuario su nombre y edad, 
y muestre por pantalla un mensaje con dichos datos en la siguiente forma: "Hola, {nombre}, tienes {edad} años".
"""

user_name = int( input("Ingrese su nombre: "))
user_year = int( input("Ingrese su edad: "))

print("Hola, {}, tienes {} años".format(user_name, user_year))