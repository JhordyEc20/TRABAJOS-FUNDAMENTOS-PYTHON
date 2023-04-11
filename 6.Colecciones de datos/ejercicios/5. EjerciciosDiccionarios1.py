#CURSO DE FUNDAMENTOS DE PYTHON 
#EJERCICIOS DE DICCIONARIOS
#Crear un diccionario vacío:
alumnos = {}
alumnos = dict()

#Agregar elementos a un diccionario:
alumnos["0110153533"] = "Veronica Chimbo"

alumnos = {
    "0106663792": "Juan Bravo",
    "1105050775": "Veronica Chimbo",
    "0107050270": "Antoni Mejia",
    "1501095408": "Pizango Jhordan",
    "0105410211": "Christian Preciado",
    "0106605017": "Astudullo Carlos",
    "0106767007": "Bruce",
    "0105737365": "Stallin Barbecho",
    "0954337572": "Torres Melanie",
    "0106637150": "Paredes Jennifer",
    "0150564078": "Danny Alex",
    "0105041982": "Adrian Piña",
    "0106399041": "Jacqueline Tenesaca",
    "0150474021": "David Ñauta"
}

alumnos["0107359788"] = "Ariel Villa"


#Acceder a un valor en un diccionario:
print(alumnos["1501095408"])

#Verificar si una llave existe en un diccionario:
print(alumnos.get("1501095406", "No se encuentra en el diccionario"))

#Eliminar un elemento de un diccionario:
alumnos.pop("0954337572")
print(alumnos.get("0954337572", "no existe"))

#Imprimir las llaves de un diccionario:
for llaves in alumnos.keys():
    print(llaves)

#Imprimir los valores de un diccionario:
for valores in alumnos.values():
    print(valores)

#Imprimir las llaves y valores de un diccionario:
for items in alumnos.items():
    print(items)
