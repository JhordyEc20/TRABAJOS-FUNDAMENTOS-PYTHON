# 11. Determinar el mayor de tres números:

user_num = int( input("Num 1 >>> "))
user_num_2 = int( input("Num 2 >>> "))
user_num_3 = int( input("Num 3 >>> "))


if (user_num > user_num_2) and (user_num > user_num_3):
    print("El numero {} es el mayor que {} y {}".format(user_num, user_num_2, user_num_3))

elif (user_num_2 > user_num) and (user_num_2 > user_num_3):
    print("El numero {} es el mayor que {} y {}".format(user_num_2, user_num, user_num_3))

elif (user_num_3 > user_num) and (user_num_3 > user_num_2):
    print("El numero {} es el mayor que {} y {}".format(user_num_3, user_num, user_num_2))

elif (user_num == user_num_2 and user_num == user_num_3):
    print("Todos los numeros tienen el mismo valor")

else:
    print("Numeros no validos.")