# 15. Programa para imprimir el día de la semana correspondiente a un número del 1 al 7:

user_num = int( input("Numero de la semana >> "))

if user_num == 1:
    print("El dia de la semana {} es lUNES!".format(user_num))

elif user_num == 2:
    print("El dia de la semana {} es MARTES!".format(user_num))

elif user_num == 3:
    print("El dia de la semana {} es MIERCOLES!".format(user_num))

elif user_num == 4:
    print("El dia de la semana {} es JUEVES!".format(user_num))

elif user_num == 5:
    print("El dia de la semana {} es VIERNES!".format(user_num))

elif user_num == 6:
    print("El dia de la semana {} es SABADO!".format(user_num))

elif user_num == 3:
    print("El dia de la semana {} es DOMINGO!".format(user_num))

else:
    print("No existe mas dias de la semana")