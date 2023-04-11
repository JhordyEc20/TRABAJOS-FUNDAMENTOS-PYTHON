# EJERCICIO 2.
''' 
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre 
por pantalla la cadena ¡Hola "nombre"!, donde "nombre" es el nombre que el usuario haya introducido.
'''

user_name = input("Como te llamas?: ")

print('''
EJERCICIO 2
Nombre: JHORDAN PIZANGO

''')

# 1
print("¡Hola! " + user_name + " :D\n")

# 2
print("¡Hola!", user_name, ":D\n")

# 3
print(f"¡Hola! {user_name} :D\n")

# 4
print("¡Hola! {} :D\n".format(user_name))
