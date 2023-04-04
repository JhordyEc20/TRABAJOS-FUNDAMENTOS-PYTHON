"""
20. Escribir un programa que pregunte al usuario una cantidad de días y 
muestre por pantalla cuantas horas, minutos y segundos hay en dicha cantidad de días.
"""

days = int( input("Numero de dias: "))

hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print("{} days are {} hours, {} minutes, and {} seconds.".format(days, hours, minutes, seconds))