#CURSO DE FUNDAMENTOS DE PYTHON 
#EJERCICIOS DE DICCIONARIOS
#1.Crea un diccionario vacío y agrega tres elementos de la siguiente forma: "clave": valor
person = {
    "Jhord Pz": 19,
    "Dalila Villipuma": 26,
    "Jimmy Ortiz": 22
}

#2.Dado el siguiente diccionario:
personas = {"Juan": 28, "María": 20, "Pedro": 32, "Ana": 25}

#a) Imprime la edad de Juan.
print(personas["Juan"])

#b) Agrega un nuevo elemento al diccionario con la clave "Luis" y la edad 18.
personas["Luis"] = 18

#c) Elimina el elemento con la clave "Pedro".
personas.pop("Pedro")

#3.Dado el siguiente diccionario:
ventas = {"manzanas": 10, "naranjas": 5, "peras": 8}

#a) Imprime la cantidad de manzanas vendidas.
print('manzanas vendidas:', ventas["manzanas"])

#b) Agrega 3 elementos más al diccionario: "limones": 12, "sandías": 3, "melones": 5.
ventas.update({
    'limones': 12, 
    'sandias': 3, 
    'melones': 5
})
print(ventas)

#c) Imprime las claves del diccionario.
print(ventas.keys())

#4. Dado el siguiente diccionario:
alumnos = {
    "Juan": {"edad": 22, "promedio": 8.5}, 
    "María": {"edad": 20, "promedio": 9.0}, 
    "Pedro": {"edad": 25, "promedio": 7.5}
}

#a) Imprime la edad de Juan.
print(alumnos["Juan"]["edad"])

#b) Imprime el promedio de María.
print(alumnos["María"]['promedio'])

#c) Agrega un nuevo elemento al diccionario con la clave "Ana" y los valores "edad": 19 y "promedio": 8.0.
alumnos["Ana"] = {
    'edad': 19,
    'promedio': 8.0
}

print(alumnos)

#5. Dado el siguiente diccionario:
empleados = {
    "Juan": {
        "departamento": "Ventas", 
        "sueldo": 1500
    },

    "María": {
        "departamento": "Contabilidad", 
        "sueldo": 1800
    },

    "Pedro": {
        "departamento": "Ventas", 
        "sueldo": 1700
    },

    "Ana": {
        "departamento": "Recursos Humanos", 
        "sueldo": 1900
    }
}

#a) Imprime el sueldo de Pedro.
print(empleados['Pedro']['sueldo'])

#b) Cambia el sueldo de Ana a 2000.
empleados["Ana"]['sueldo'] = 2000
print(empleados)

#c) Crea un nuevo diccionario con los empleados del departamento de Ventas.

print('*'*12)
empleados_ventas = {}
for name, depar in empleados.items():
    if depar['departamento'] is 'Ventas':
        empleados_ventas[name] = depar

print(empleados_ventas)


'''
!NO HABIAN DATOS PARA RESOLVER LOS EJERCICIOS DE ABAJO ASI QUE ME LOS INVENTE

'''
#6.Dado el siguiente diccionario:
estudiantes = {
"Pedro": ["Matemáticas", "Biologia", "Historia"],
"María": ["Física", "Química", "Inglés"]
}
#a) Imprime las materias en las que está inscrito Pedro.
print(estudiantes["Pedro"])

#b) Agrega una materia más a la lista de materias de María: "Programación".
estudiantes["María"].append("Programacion")
print(estudiantes)

#c) Crea un nuevo diccionario con los estudiantes que están inscritos en la materia de Biología.
estudiantes_biologia = {}

for estudi, materias in estudiantes.items():
    if 'Biologia' in materias:
        estudiantes_biologia[estudi] = materias

print('*'*25)
print(estudiantes_biologia)

#7. Dado el siguiente diccionario:
frutas = {
    "manzanas": {
        "precio": 1.2, 
        "stock": 10
    },

    "naranjas": {
        "precio": 0.8, 
        "stock": 15
    },

    "peras": {
        "precio": 1.5, 
        "stock": 8
    }
}

#a) Imprime el precio de las naranjas.
print(frutas["naranjas"]['precio'])

#b) Cambia el stock de peras a 12.
frutas["peras"]['stock'] = 12
print(frutas)

#c) Crea una función que calcule el valor total de los productos en el diccionario.
def calcular_valor_dict(date_user):
    suma = 0
    for clave, valor in date_user.items():
         suma += valor['precio']
    
    print('suma de precios', suma)

calcular_valor_dict(frutas)