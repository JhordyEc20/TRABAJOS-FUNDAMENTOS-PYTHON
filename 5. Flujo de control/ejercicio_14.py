# 14. Programa para determinar si un número es divisible por 4 y 6:

user_num = int( input("Num >>> "))

if (user_num % 4 == 0)  and (user_num % 6 == 0):
    print("El numero {} es divisible por 4 y 6".format(user_num))
else:
    print("El numero {} no es divisible por 4 y 6!!!".format(user_num))