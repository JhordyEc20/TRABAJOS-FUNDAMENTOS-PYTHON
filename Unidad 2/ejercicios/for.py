###CURSO DE FUNDAMENTOS DE PYTHON
#Trabajar los ejercicios con funciones, para llamarlos deberá de crear un menu en el que le permitira seleccionar al usuario que ejercicios ejecutar.
#1. Suma de elementos de una lista: Dada una lista de números, escribe un programa que calcule la suma de todos los elementos de la lista usando un bucle for.
def suma_lista(lista):
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma
#2. Contar elementos en una lista: Dada una lista de elementos, escribe un programa que cuente cuántos elementos hay en la lista usando un bucle for.
def contar_elementos(lista):
    contador = 0
    for elemento in lista:
        contador += 1
    return contador

#3. Imprimir elementos de una lista: Dada una lista de elementos, escribe un programa que imprima cada elemento de la lista en una línea separada usando un bucle for.
def imprimir_elementos(lista):
    for elemento in lista:
        print(elemento)

#4. Contar caracteres en una cadena: Dada una cadena de caracteres, escribe un programa que cuente cuántos caracteres hay en la cadena usando un bucle for.
def contar_caracteres(cadena):
    contador = 0
    for caracter in cadena:
        contador += 1
    return contador

#5. Imprimir caracteres de una cadena: Dada una cadena de caracteres, escribe un programa que imprima cada carácter de la cadena en una línea separada usando un bucle for.
def imprimir_caracteres(cadena):
    for caracter in cadena:
        print(caracter)

#6. Imprimir los primeros N números naturales: Dado un número entero N, escribe un programa que imprima los primeros N números naturales usando un bucle for.
def imprimir_naturales(n):
    for i in range(1, n+1):
        print(i)

#7. Imprimir los primeros N números pares: Dado un número entero N, escribe un programa que imprima los primeros N números pares usando un bucle for.
def imprimir_pares(n):
    for i in range(2, n*2+1, 2):
        print(i)

#8. Imprimir los primeros N números impares: Dado un número entero N, escribe un programa que imprima los primeros N números impares usando un bucle for.
def imprimir_impares(n):
    for i in range(1, n*2, 2):
        print(i)
#9. Imprimir la tabla de multiplicar de un número: Dado un número entero N, escribe un programa que imprima la tabla de multiplicar de N usando un bucle for.
def tabla_multiplicar(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n*i)

#10. Imprimir los primeros N números de la serie de Fibonacci: Dado un número entero N, escribe un programa que imprima los primeros N números de la serie de Fibonacci usando un bucle for.
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a)
        c = a + b
        a = b
        b = c


def menu():

    print("Ejercicios:")
    print("1. Suma de elementos de una lista")
    print("2. Contar elementos en una lista")
    print("3. Imprimir elementos de una lista")
    print("4. Contar caracteres en una cadena")
    print("5. Imprimir caracteres de una cadena")
    print("6. Imprimir los primeros N números naturales")
    print("7. Imprimir los primeros N números pares")
    print("8. Imprimir los primeros N números impares")
    print("9. Imprimir la tabla de multiplicar de un número")
    print("10. Imprimir los primeros N números de la serie de Fibonacci")
    print("0. Salir")

    opcion = int(input("Selecciona un ejercicio (0-10): "))
    
    
    while opcion != 0:
        if opcion == 1:
            lista = [1, 2, 3, 4, 5]
            print("La suma de los elementos de la lista es:", suma_lista(lista))
        elif opcion == 2:
            lista = [1, 2, 3, 4, 5]
            print("La lista tiene", contar_elementos(lista), "elementos")
        elif opcion == 3:
            lista = [1, 2, 3, 4, 5]
            imprimir_elementos(lista)
        elif opcion == 4:
            cadena = "Hola mundo"
            print("La cadena tiene", contar_caracteres(cadena), "caracteres")
        elif opcion == 5:
            cadena = "Hola mundo"
            imprimir_caracteres(cadena)
        elif opcion == 6:
            n = int(input("Ingrese un número entero N: "))
            imprimir_naturales(n)
        elif opcion == 7:
            n = int(input("Ingrese un número entero N: "))
            imprimir_pares(n)
        elif opcion == 8:
            n = int(input("Ingrese un número entero N: "))
            imprimir_impares(n)
        elif opcion == 9:
            n = int(input("Ingrese un número entero N: "))
            tabla_multiplicar(n)
        elif opcion == 10:
            n = int(input("Ingrese un número entero N: "))
            fibonacci(n)
        else:
            print("Opción inválida")

menu()