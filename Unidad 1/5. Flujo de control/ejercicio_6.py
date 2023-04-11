'''
#### 6. 
Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:

- Mostrar una suma de los dos números
- Mostrar una resta de los dos números (el primero menos el segundo)
- Mostrar una multiplicación de los dos números
- En caso de introducir una opción inválida, el programa informará de que no es correcta.


'''
print('''
FUNDAMENTOS DE PROGRAMACION
NOMBRE: Jhordan Pizango
31/03/2023

''')

mensaje = '''
REALIZAR OPERACIONES ARITMETICAS

+ --> SUMA
- --> RESTA
* --> Multiplicacion
--> '''


num_1 = int( input("Num 1: "))
num_2 = int( input("Num 2: "))
user_option = input(mensaje)


if user_option == "+":
    # SUMA
    print("La SUMA de los numeros {} y {} es: {}".format(num_1, num_2, (num_1+num_2)))
          
elif user_option == "-":
    # RESTA
    print("La RESTA de los numeros {} y {} es: {}".format(num_1, num_2, (num_1-num_2)))
          
elif user_option == "*":
    # MULTIPLICACION
    print("La MULTIPLICACION de los numeros {} y {} es: {}".format(num_1, num_2, (num_1*num_2)))
          
else:
    print("¡Opcion Invalida!")

