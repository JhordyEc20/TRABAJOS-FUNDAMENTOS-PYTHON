print('''
OPCION DE SEMAFORO

v --> Verde
r --> Rojo
a --> Amarrillo

''')

semaforo = input("Elige un color de semaforo: ")

if semaforo == "v":
    print("Pasa el peaton🙍‍♂️")
elif semaforo == "a":
    print("Veiculo reduce la velocidad🚦")
elif semaforo == "r":
    print("Pasa el veiculo🚗")
else:
    print("Opcion incorrecta :D!")


