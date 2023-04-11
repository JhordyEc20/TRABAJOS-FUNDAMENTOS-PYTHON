#1
def contador_ascendente(num):
    i = 0
    limit = 5
    
    while i <= limit:
        num = num + i 
        print(num)
        i += 1

#2
def contador_decendente(num):
    i = 5
    limit = 0

    while i > limit:
        i -= 1
        num = num - 1
        print(num)
 

#3
def suma_numeros(num):
    i = 0
    limit = 5
    
    while i <= limit:
        suma = num + i 
        i += 1
    
    print(suma)

#4
def factorial(num):
    i = 0
    fact = 1

    while i <= num:
        fact = fact * i
        i += 1

    print(fact) 
#5
def adivinar_numero():
    num_adv = 5
    num = 0

    while num_adv != num:
        num = int( input("Ingresa numero: "))
        if num_adv == num:
            print("Tu numero: {} numero a divinar {}, acertaste!.".format(num, num_adv))
        else:
            print("Tu numero: {} numero {}, no acertaste!".format(num, num_adv))

#6
def contador_vocales(user_str):
    vocales = "aeiou"

    i = 0
    limit = len(user_str)
    print(limit)

    num_vocales = 0

    while i <= limit:
        if user_str[i] in vocales:
            num_vocales += 1
        i += 1
        
    print("Numeros de vocales {}".format(num_vocales))

#7
def suma_numeros_pares():
    return "7. Suma de numeros pares"

#8
def calculo_potencial():
    return "8. calculo de potencial"

#9
def calculo_promedio():
    return "9. calculo de promedio"

#10
def contador_palabras():
    return "10. Contador de palabras"


opcion = 0

while (opcion >= 0) and (opcion <= 10):
    print("#"*8, "MENU OPCIONES", "#"*8)
    print("1. Contador Ascendente")
    print("2. Contador Decendente")
    print("3. Suma de numeros")
    print("4. Factorial")
    print("5. Adivinar numero")
    print("6. Contador de vocales")
    print("7. Suma de numeros pares")
    print("8. Calculo de potencia")
    print("9. Calculo de promedio")
    print("10. Contador de palabras")
    print("0. Salir")
    

    opcion = int( input("Opcion: "))
    # opciones

    # 1. Contador Ascendente
    if opcion == 1:
        user_num = int( input("Ingrese numero: "))
        contador_ascendente(user_num)

    elif opcion == 2:
        user_num = int( input("Ingrese numero: "))
        contador_decendente(user_num)

    elif opcion == 3:
        user_num = int( input("Ingrese numero: "))
        suma_numeros(user_num)

    elif opcion == 4:
        user_num = int( input("Ingrese numero: "))
        factorial(user_num)

    elif opcion == 5:
        user_num = int( input("Ingrese numero: "))
        adivinar_numero()

    elif opcion == 6:
        user_str = input("Ingrese frase: ")
        contador_vocales(user_str)

    elif opcion == 7:
        print( suma_numeros_pares())
    
    elif opcion == 8:
        print( calculo_potencial())

    elif opcion == 9:
        print( calculo_promedio)

    elif opcion == 10:
        print( contador_palabras)
    
    elif opcion == 0:
        break
    
    else:
        print("Opcion incorrecta")
    break



