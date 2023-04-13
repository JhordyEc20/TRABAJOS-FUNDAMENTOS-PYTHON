#CURSO DE FUNDAMENTOS DE PYTHON 
#EJERCICIOS DE CONJUNTOS
#Crear un conjunto con los números del 1 al 10 e imprimirlo en pantalla.
numeros = set( range(1, 11))
print(type(numeros))
print(numeros)

#Crear dos conjuntos, uno con los números pares del 1 al 10 y otro con los impares del 1 al 10. Luego, imprimir los conjuntos y la intersección entre ellos.
numeros_pares = set( range(1, 10))
numeros_impares = set( range(1, 10))
print("pares:", numeros_pares)
print("impares:", numeros_impares)
print("Intersección entre los conjuntos:", numeros_pares.intersection(numeros_impares))

#Crear un conjunto con los elementos "manzana", "banana" y "naranja". Luego, pedirle al usuario que ingrese un elemento y determinar si ese elemento se encuentra en el conjunto o no.
frutas = {"manzana", "banana", "naranja"}
fruta_ingresada = input("Ingrese una fruta: ")
if fruta_ingresada in frutas:
    print("La fruta ingresada se encuentra en el conjunto.")
else:
    print("La fruta ingresada no se encuentra en el conjunto.")

#Crear un conjunto con los números del 1 al 5 y otro con los números del 4 al 8. Luego, unir los conjuntos y eliminar los elementos repetidos. Finalmente, imprimir el conjunto resultante.
numeros_1 = set( range(1, 5))
numeros_2 = set( range(4, 8))
numeros_union = numeros_1.union(numeros_2)
numeros_sin_repetir = numeros_union
print(numeros_sin_repetir)

#Crear un conjunto con los elementos "leche", "pan", "huevos" y "azúcar". Luego, eliminar el elemento "azúcar" del conjunto y agregar el elemento "harina". Finalmente, imprimir el conjunto resultante.
compras = {"leche", "pan", "huevos", "azúcar"}
compras.remove("azúcar")
compras.add("harina")
print(compras)


#Crear un conjunto con los nombres "Juan", "María", "Pedro" y "Luisa". Luego, imprimir el número de elementos del conjunto.
nombres = {"Juan", "María", "Pedro", "Luisa"}
print("Número de elementos:", len(nombres))

#Crear dos conjuntos, uno con los números del 1 al 5 y otro con los números del 4 al 8. Luego, imprimir los conjuntos y la diferencia simétrica entre ellos.
numeros_1 = set( range(1, 5))
numeros_2 = set( range(4, 8))
print("Conjunto 1:", numeros_1)
print("Conjunto 2:", numeros_2)
diferencia_simetrica = numeros_1.symmetric_difference(numeros_2)
print("Diferencia simétrica:", diferencia_simetrica)

#Crear un conjunto con los números del 1 al 10 y otro con los números del 5 al 15. Luego, imprimir los conjuntos y la unión entre ellos.
numeros_1 = set( range(1, 11))
numeros_2 = set( range(5, 16))

print("Conjunto 1:", numeros_1)
print("Conjunto 2:", numeros_2)
union = numeros_1.union(numeros_2)
print("Unión de los conjuntos:", union)

#Crear un conjunto con los elementos "manzana", "banana", "naranja" y "pera". Luego, imprimir los elementos del conjunto en orden alfabético.
frutas = {"manzana", "banana", "naranja", "pera"}
#sorted ordenamos el orden alfaberico en otra variable
frutas_ordenadas = sorted(frutas)
print(frutas_ordenadas)

#Crear un conjunto con los números del 1 al 10 y otro con los números del 6 al 15. Luego, imprimir los conjuntos y la intersección entre ellos.
numeros_1 = set( range(1, 10))
numeros_2 = set( range(6, 15))
print("Conjunto 1:", numeros_1)
print("Conjunto 2:", numeros_2)
interseccion = numeros_1.intersection(numeros_2)
print("Intersección de los conjuntos:", interseccion)