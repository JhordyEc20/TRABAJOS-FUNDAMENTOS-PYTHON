'''
* Nombre del empleado
* Departamentos pertenece
* Antiguedad

OPCIONES

1.DEPARTAMENTO ATENCION AL CLIENTE
2.DEPARTAMENTO DE LOGISTICA
3.DEPARTAMENTO DE GERENCIA

1 AÑO DE SERVICIO -->  6 DIAS DE VACACIONES
2 A 6 AÑOS        --> 12 DIAS DE VACACIONES
MAYOR A 7 AÑOS    --> 20 DIAS DE VACACIONES
'''
mensaje = '''
A que departamento perteneces?
1 --> DEPARTAMENTO ATENCION AL CLIENTE
2 --> DEPARTAMENTO DE LOGISTICA
3 --> DEPARTAMENTO DE GERENCIA
>>> '''

name = input("Nombre: ")
depar = int( input(mensaje))
antiguedad = int( input("¿Cuantos años trabajaste?: "))

if depar == 1:
    if antiguedad == 1:
        vaca = "Tienes 6 dias de vacaciones! Disfrutalo"
    elif antiguedad >= 2 and antiguedad <= 6:
        vaca = "Tienes 12 dias de vacaciones! Disfrutalo"
    else:
        vaca = "Tienes 20 dias de vacaciones! Disfrutalo"

elif depar == 2:
    if antiguedad == 1:
        vaca = "Tienes 7 dias de vacaciones! Disfrutalo"
    elif antiguedad >= 2 and antiguedad <= 6:
        vaca = "Tienes 14 dias de vacaciones! Disfrutalo"
    else:
        vaca = "Tienes 22 dias de vacaciones! Disfrutalo"
elif depar == 3:
    if antiguedad == 1:
        vaca = "Tienes 10 dias de vacaciones! Disfrutalo"
    elif antiguedad >= 2 and antiguedad <= 6:
        vaca = "Tienes 20 dias de vacaciones! Disfrutalo"
    else:
        vaca = "Tienes 30 dias de vacaciones! Disfrutalo"
else:
    print("Opcion Invalida X")
    exit()

print('''
*****************************************************
EMPLEADO
NOMBRE: {}
DEPARTAMENTO: {}
ANTIGUEDAD: {}
VACACIONES: {}
'''.format(name, depar, antiguedad, vaca))