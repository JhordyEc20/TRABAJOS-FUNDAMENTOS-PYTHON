print("""
#### 5.
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

RENTA                        % de Impuestos
Menos de $10000                    5%
Entre $10000 y $20000              15%
Entre $20000 y $35000              20%
Entre $35000 y $60000              30%
Mas de $60000                      45%


Realizar un programa que pueda decir el % de impuestos que una persona deba pagar según su sueldo

""")

declara = int( input("Cuanto declaras?: "))

if declara < 10000:
    # 5%
    print(f"Pagas ${(declara*5)/100} Dolares de Impuestos.")

elif declara >= 10000 and declara < 20000:
    # 15%
    print(f"Pagas ${(declara*15)/100} Dolares de Impuestos.")

elif declara >= 20000 and declara < 35000:
    # 20%
    print(f"Pagas ${(declara*20)/100} Dolares de Impuestos.")

elif declara >= 35000 and declara < 60000:
    # 30%
    print(f"Pagas ${(declara*30)/100} Dolares de Impuestos.")

else:
    # 45%
    print(f"Pagas ${(declara*45)/100} Dolares de Impuestos.")
    