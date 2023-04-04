"""
18. Escribir un programa que pida al usuario una frase y determine si es un palíndromo. Ignorar espacios en blanco y mayúsculas/minúsculas al determinar si la frase es un palíndromo o no.
-Un palíndromo es una palabra, número o frase que se lee igual de izquierda a derecha que de derecha a izquierda. Por ejemplo, "ana", "radar" y "aibohphobia" son palíndromos.
"""

user_frase = input("Ingrese una frase: ")

frase_sin_espacios = user_frase.replace(" ", "").lower()

if frase_sin_espacios == frase_sin_espacios[::-1]:
    print("La frase {} es un palíndromo.".format(user_frase))
else:
    print("La frase {} no es un palíndromo.".format(user_frase))
