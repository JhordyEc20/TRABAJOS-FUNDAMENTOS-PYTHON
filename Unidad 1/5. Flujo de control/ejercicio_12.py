# 12. Programa para determinar si un número es positivo, negativo o cero:

user_num = int( input("Num >>> "))

if user_num > 0:
    print("El numero {} es positivo".format(user_num))
elif user_num < 0:
    print("El numero {} es negativo".format(user_num))
else:
    print("El numero {} es cero".format(user_num))