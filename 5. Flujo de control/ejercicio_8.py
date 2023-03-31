'''

#### 8.
Escribí un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje 
“Es vocal”. Verificar si el usuario ingresó un string de más de un carácter y, en ese caso, informarle que no se 
puede procesar el dato.

'''
print('''
PROGRAMA
ES UNA LETRA DEL ABECEDARIO?''')

letra_user = input("letra: ").lower()
abecedario_minus = "abcdefghijklmnñopqrstuvwxyz"


if len(letra_user) != 1:
    print("No se puede procesar el dato")
    exit()
else:
    if letra_user in abecedario_minus:
        print("Es una letra de abecedario")
    else:
        print("No es una letra del abecedario")