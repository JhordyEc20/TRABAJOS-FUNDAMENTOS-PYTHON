# 13. Programa para determinar si un número es múltiplo de 3:

user_num = int( input("Num: "))

if user_num % 3 == 0:
    print("El numero {} es divicible para 3".format(user_num))
    
else:
    print("El numero {} no es un numero divicible de 3".format(user_num))