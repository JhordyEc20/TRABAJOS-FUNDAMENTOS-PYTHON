'''
#### 7.
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
Los ingredientes para cada tipo de pizza aparecen a continuación.

- Ingredientes vegetarianos: Pimiento y tofu.
- Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta 
le muestre un menú con los ingredientes disponibles para que elija. 

Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
Al final se debe mostrar por pantalla si la pizza elegida es 
vegetariana o no y todos los ingredientes que lleva.
'''

mensaje = '''
¿Quieres una Pizza Vegetariana?
>>> '''

mensaje_2 = '''
¿Deseas ingredeintes adicionales?
>>> '''

mensj_ingrediente_adici_vege = '''
Elige un Ingrediente adicional
1 --> Pimiento
2 --> Tofu
>>>'''

opcion = input(mensaje).lower()

if opcion == "si":
    # Pizza Vegetariana
    print('''
    MUY BIEN!
    *****************************
    INGREDIENTES DE TU PIZZA
    - Mozzarella
    - Tomate
    
    *****************************''')
    ingrediente_adicional = input(mensaje_2).lower()

    if ingrediente_adicional == "si":
        
        ingrediente = int( input(mensj_ingrediente_adici_vege))
        if ingrediente == "1":
            # Pimiento
            pass
        elif ingrediente == "2":
            # TOFU
            pass
    else:
        print('''
        ************************************
        PEDIDO FINALIZADO

        TIPO DE PIZZA: PIZZA BASIC
        TU PIZZA ES: VEGETARIANA
        INGREDIENTES: MOZZARELLA, TOMATE

        ¡GRACIAS POR TU PIZZA!''')


elif opcion == "no":
    # Pizza Normal
    pass

else:
    print("¡Opcion Incorrecta!")



