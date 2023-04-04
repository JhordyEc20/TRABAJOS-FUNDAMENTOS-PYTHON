"""
10. Determinar si un año es bisiesto.
Es divisible entre 4, pero no es divisible entre 100.
Es divisible entre 400.

Por ejemplo, los años 2000 y 2020 son bisiestos porque son divisibles entre 400, 
mientras que el año 1900 no es bisiesto porque es divisible entre 100 pero no entre 400.
"""

user_year = int(input("AÑO: "))

if (user_year % 4 == 0) and (user_year % 100 != 0):
    if user_year % 400 == 0:
        print("EL AÑO {} ES UN AÑO BISIESTO!!!".format(user_year))
        
    else:
        print("EL AÑO {} NO ES BISIESTO".format(user_year))

else:
    print("EL AÑO {} NO ES BISIESTO".format(user_year))

