#CURSO DE FUNDAMENTOS DE PYTHON 
#EJERCICIOS DE TUPLAS
#Crear una tupla de números enteros y calcular su suma y promedio.
tpl_num = (7, 5, 3, 9, 4)
print('Promedio: {}'.format( sum(tpl_num) / len(tpl_num) ))

#Crear dos tuplas de la misma longitud y crear una nueva tupla que contenga la suma de los elementos correspondientes de ambas tuplas.
tpl_1 = (3, 5, 7, 8, 4)
tpl_2 = tuple( range(1, 5))

tpl_sum = sum(tpl_1 + tpl_2)
print(tpl_sum)

#Crear una tupla de nombres y ordenarla alfabéticamente.
names = ('Jhordan', 'Marisol', 'Marcos', 'Romina')
print(sorted(names))

#Crear una tupla de números y encontrar el valor mínimo y máximo.
tpl_num = tuple( range(1, 15))
print(min( tpl_num), max(tpl_num))

#Crear una tupla de números y convertirla en una lista.
tpl_num_list = tpl_num
print( type(tpl_num))

#Crear una tupla con los días de la semana y mostrar el tercer elemento.
dias_semana = ('lunes', 'martes', 'miercoles', 'jueves', 'viernes')
print( dias_semana[2])

#Crear una tupla con números enteros y mostrar aquellos que son pares.
nums = tuple( range(1, 20))

for num_element in nums:
        if num_element % 2 is 0:
                print(num_element)


#Crear una tupla con los meses del año y mostrar aquellos que tienen más de cinco letras.
meses = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')

for mes in meses:
        if len(mes) > 5:
                print(mes)

#Crear una tupla con las edades de varias personas y mostrar la cantidad de personas mayores de 18 años.
edades = (23, 17, 30, 12, 41, 18, 20, 15, 27, 19)

num_person = 0
for edad in edades:
        if edad > 18:
            num_person += 1
print('Hay {} mayores de 18 años'.format(num_person))

#Crear una tupla de tuplas que contienen información de libros y mostrar el título del tercer libro.

libros = ('El señor de los anillos', 'J.R.R. Tolkien', 'Cien años de soledad', 'Gabriel García Márquez', 'Don Quijote de la Mancha', 'Miguel de Cervantes')

print("Tercer libro es:", libros[2])