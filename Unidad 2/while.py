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
def suma_numeros_pares(num):
    suma = 0
    if num % 2 == 0:
        suma += num
    print(suma)

#8
def calculo_potencial(num, exp):
    print(num**exp)

#9
def calculo_promedio(num):
    num = num.split(',')

    suma = []
    i = 0

    while i < len(num):
        suma.append(int( num[i]))
        i += 1

    prom = sum(suma) / len(num)
    print('Promedio', prom) 

#10
def contador_palabras(user_frase):
    caract = 0
    i = 0

    while i < len(user_frase):
        if user_frase[i] == " ":
            caract += 1
        i += 1

    print('Hay {} caracteres'.format(caract))


opcion = 0
menu = '''
1. Contador Ascendente
2. Contador Decendente
3. Suma de numeros
4. Factorial
5. Adivinar numero
6. Contador de vocales
7. Suma de numeros pares
8. Calculo de potencia
9. Calculo de promedio
10. Contador de palabras
0. Salir
>>> '''

while (opcion >= 0) and (opcion <= 10):
    print('#'*8 + 'MENU OPCIONES' + '#'*8)
    opcion = int( input(menu))
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
        user_num = int( input("Ingrese numero: "))
        suma_numeros_pares(user_num)
    
    elif opcion == 8:
        user_num = int( input("Ingrese numero: "))
        user_exp = int( input("Ingrese exponente: "))
        calculo_potencial(user_num, user_exp)

    elif opcion == 9:
        user_num = input("Ingrese notas: ")
        calculo_promedio(user_num)

    elif opcion == 10:
        user_frase = input("Ingrese frase: ")
        contador_palabras(user_frase)
    
    elif opcion == 0:
        break
    
    else:
        print("Opcion incorrecta")
    break