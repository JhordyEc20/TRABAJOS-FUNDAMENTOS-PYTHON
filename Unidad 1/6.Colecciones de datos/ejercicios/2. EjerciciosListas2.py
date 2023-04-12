#CURSO DE FUNDAMENTOS DE PYTHON 
#EJERCICIOS DE LISTAS A RESOLVER
#Crea una lista vacía llamada numeros e introduce los números del 1 al 5. Luego, muestra la lista por pantalla.
lista = []

lista.extend([1, 2, 3, 4, 5])

print(lista)

#Crea una lista con los nombres de tus amigos y muestra por pantalla el primer elemento de la lista.
friends = ['Daly', 'Jhord', 'Zaph']
print(friends[0])


#Crea una lista con los números del 1 al 10 y muestra por pantalla los números pares.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numeros:
    if num % 2 is 0:
        print(num)

#Crea una lista con los nombres de tus amigos y muestra por pantalla el último elemento de la lista.
friends = ['Daly', 'Jhord', 'Zaph']
print(friends[2])


#Crea una lista con los números del 1 al 10 y muestra por pantalla el último elemento de la lista.
l_num = list( range(1, 10))
#slicen
print(l_num[-1])


#Crea una lista con los números del 1 al 10 y muestra por pantalla los números impares.
l_num2 = list( range(1, 10))

for num in l_num2:
    if num % 2 != 0:
        print(num)


#Crea una lista con los nombres de tus amigos y añade un nuevo amigo a la lista. Luego, muestra la lista por pantalla.
friends = ['Daly', 'Jhord', 'Zaph']
friends.append("Romi")

print(friends)


#Crea una lista con los números del 1 al 10 y muestra por pantalla el primer y el último elemento de la lista.
l_num3 = list( range(1, 10))
print(l_num3[0], l_num3[-1])


#Crea una lista con los nombres de tus amigos y muestra por pantalla el número de elementos de la lista.
print(len(friends))


#Crea una lista con los números del 1 al 10 y muestra por pantalla la suma de todos los elementos de la lista.
print( sum(l_num3))