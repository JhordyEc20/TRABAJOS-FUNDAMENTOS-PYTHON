#para el ejercicio #5
import random


###CURSO DE FUNDAMENTOS DE PYTHON
#Trabajar los ejercicios con funciones, para llamarlos deberá de crear un menu en el que le permitira seleccionar al usuario que ejercicios ejecutar.
#1.Contador ascendente: # Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, cuente desde cero hasta ese número, imprimiendo cada número en la pantalla.
def contador_ascendente():
    num = int(input("Ingrese un número entero positivo: "))
    i = 0
    while i <= num:
        print(i)
        i += 1

#2.Contador descendente: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, cuente desde ese número hasta cero, imprimiendo cada número en la pantalla.
def contador_descendente():
    num = int(input("Ingrese un número entero positivo: "))
    i = num
    while i >= 0:
        print(i)
        i -= 1

#3.Suma de números: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, calcule la suma de todos los números desde cero hasta ese número y lo imprima en la pantalla.
def suma_numeros():
    num = int(input("Ingrese un número entero positivo: "))
    suma = 0
    i = 0
    while i <= num:
        suma += i
        i += 1
    print("La suma de todos los números desde 0 hasta", num, "es", suma)

#4.Factorial: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, calcule el factorial de ese número y lo imprima en la pantalla. El factorial de un número n se define como el producto de todos los números enteros desde 1 hasta n.
def factorial():
    num = int(input("Ingrese un número entero positivo: "))
    factorial = 1
    i = 1
    while i <= num:
        factorial *= i
        i += 1
    print("El factorial de", num, "es", factorial)

#5.Adivinar un número: Escribe un programa en Python que genere un número aleatorio entre 1 y 100, y pida al usuario que adivine ese número. Si el usuario ingresa un número mayor al número generado, el programa debe imprimir "El número que buscas es menor". Si el usuario ingresa un número menor al número generado, el programa debe imprimir "El número que buscas es mayor". Si el usuario adivina el número, el programa debe imprimir "¡Felicitaciones, adivinaste el número!" y terminar.
def adivinar_numero():
    num_aleatorio = random.randint(1, 100)
    while True:
        num = int(input("Ingresa un número entre 1 y 100: "))
        if num > num_aleatorio:
            print("El número que buscas es menor.")
        elif num < num_aleatorio:
            print("El número que buscas es mayor.")
        else:
            print("¡Felicitaciones, adivinaste el número!")
            break

#6.Contador de vocales: Escribe un programa en Python que pida al usuario una cadena de texto y, utilizando un bucle while, cuente la cantidad de vocales que tiene esa cadena. Para simplificar el problema, puedes considerar que la cadena solo contiene letras minúsculas.
def contar_vocales():
    cadena = input("Ingresa una cadena de texto: ")
    vocales = "aeiou"
    contador = 0
    i = 0
    while i < len(cadena):
        if cadena[i] in vocales:
            contador += 1
        i += 1
    print("La cadena tiene", contador, "vocales.")

#7.Suma de números pares: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, calcule la suma de todos los números pares desde cero hasta ese número y lo imprima en la pantalla.
def suma_numeros_pares():
    n = int(input("Ingresa un número entero positivo: "))
    suma = 0
    i = 0
    while i <= n:
        if i % 2 == 0:
            suma += i
        i += 1
    print("La suma de los números pares desde 0 hasta", n, "es:", suma)

#8.Cálculo de potencia: Escribe un programa en Python que pida al usuario dos números enteros positivos: una base y un exponente. Utilizando un bucle while, calcule la potencia de la base elevada al exponente y lo imprima en la pantalla.
def calcular_potencia():
    base = int(input("Ingresa la base: "))
    exponente = int(input("Ingresa el exponente: "))
    resultado = 1
    i = 1
    while i <= exponente:
        resultado *= base
        i += 1
    print(base, "elevado a", exponente, "es igual a", resultado)

#9.Cálculo de promedio: Escribe un programa en Python que pida al usuario una lista de números y, utilizando un bucle while, calcule el promedio de esos números y lo imprima en la pantalla.
def calcular_promedio():
    numeros = []
    total = 0
    contador = 0
    seguir_ingresando = True
    while seguir_ingresando:
        numero = input("Ingresa un número o 'fin' para terminar: ")
        if numero == "fin":
            seguir_ingresando = False
        else:
            numeros.append(float(numero))
            total += float(numero)
            contador += 1
    promedio = total / contador
    print("El promedio de los números ingresados es:", promedio)

#10.Contador de palabras: Escribe un programa en Python que pida al usuario una cadena de texto y, utilizando un bucle while, cuente la cantidad de palabras que tiene esa cadena. Para simplificar el problema, puedes considerar que las palabras están separadas por espacios en blanco.
def contar_palabras():
    texto = input("Ingresa un texto: ")
    cantidad_palabras = 0
    indice = 0
    while indice < len(texto):
        if texto[indice] == " ":
            cantidad_palabras += 1
        indice += 1
    cantidad_palabras += 1
    print("El texto ingresado tiene", cantidad_palabras, "palabras.")


while True:
    print("1. Contador ascendente")
    print("2. Contador descendente")
    print("3. Suma de números")
    print("4. Factorial")
    print("5. Adivinar un número")
    print("6. Contador de vocales")
    print("7. Suma de números pares")
    print("8. Cálculo de potencia")
    print("9. Cálculo de promedio")
    print("10. Contador de palabras")
    print("0. Salir")

    opcion = int( input("Ingrese el número de ejercicio que desea ejecutar (0 para salir): "))

    if opcion == 1:
        contador_ascendente()
    elif opcion == 2:
        contador_descendente()
    elif opcion == 3:
        suma_numeros()
    elif opcion == 4:
        factorial()
    elif opcion == 5:
        adivinar_numero()
    elif opcion == 6:
        contar_vocales()
    elif opcion == 7:
        suma_numeros_pares()
    elif opcion == 8:
        calcular_potencia()
    elif opcion == 9:
        calcular_promedio()
    elif opcion == 10:
        contar_palabras(8)
    elif opcion == 0:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, elija una opción del menú.")

    print('\n')
    print('*'* 29)