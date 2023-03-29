#Realizar un ejercicio que le 2 numeros por teclado y determine los siguientes aspectos (es suficiente con mostrar True o False)

#- Si los dos números son iguales 
#- Si los dos números son diferentes 
#- Si el primero es mayor que el segundo 
#- Si el segundo es mayor o igual que el primero

a = int( input("Numero 1: "))
b = int( input("Numero 2: "))

print('''
EJERCICIO 1

CURSO FUNDAMENTOS DE PYTHON

Nombre: Jhordan Pizango
''')

# 1
print("Si los dos numeros" + str(a) + " y " + str(b) + " son iguales?: " + str(a == b) + "\n")

# 2
print("Si los dos numeros", a, "y", b, "son diferentes?:", str(a != b), "\n")

#3
print(f"Si el primero {a} es mayor que el segundo {b}?: {a > b} \n")

#4
print("Si el segundo {} es mayor o igual que el primero {}: {} \n".format(b, a, b >= a))

