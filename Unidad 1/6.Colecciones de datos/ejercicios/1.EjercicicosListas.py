###CURSO DE FUNDAMENTOS DE PYTHON
#1. Crear una lista de numeros del 1 al 5
lista = [1, 2, 3, 4, 5]


#2. Accede al elemto 3 de la lista:
print(lista[2])


#3. Modifica un elemento de la lista:
lista[3] = 10
print(lista[3])


#4. Agrega el elemento 9 al final de la lista
lista.append(22)


#5. Eliminar el elemento 2 de la lista:
lista.pop(1)
print(lista)


#6. Recorrer una lista con un bucle for:
for element in lista:
    print(element)


#7. Ordenar una lista:
lista.sort()


#8. Obtener la longitud de una lista:
print(len(lista))


#9. Comprobar si un elemento está en la lista:
print(5 in lista)


#10. presentar el numero minimo
print(min(lista))

#11. Presentar el numero maximo
print(max(lista))