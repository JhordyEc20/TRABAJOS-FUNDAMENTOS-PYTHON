# 16. Programa para imprimir el nombre del mes correspondiente a un número del 1 al 12:

num_mes = int(input("Num del 1 al 12: "))

if num_mes == 1:
    print("El mes {} es Enero".format(num_mes))
elif num_mes == 2:
    print("El mes {} es Febrero".format(num_mes))
elif num_mes == 3:
    print("El mes {} es Marzo".format(num_mes))
elif num_mes == 4:
    print("El mes {} es Abril".format(num_mes))
elif num_mes == 5:
    print("El mes {} es Mayo".format(num_mes))
elif num_mes == 6:
    print("El mes {} es Junio".format(num_mes))
elif num_mes == 7:
    print("El mes {} es Julio".format(num_mes))
elif num_mes == 8:
    print("El mes {} es Agosto".format(num_mes))
elif num_mes == 9:
    print("El mes {} es Septiembre".format(num_mes))
elif num_mes == 10:
    print("El mes {} es Octubre".format(num_mes))
elif num_mes == 11:
    print("El mes {} es Noviembre".format(num_mes))
elif num_mes == 12:
    print("El mes {} es Diciembre".format(num_mes))
else:
    print("Número de mes inválido")