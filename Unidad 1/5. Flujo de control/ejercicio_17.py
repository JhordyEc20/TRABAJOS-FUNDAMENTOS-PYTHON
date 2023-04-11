"""
17. Escribir un programa que pida al usuario una nota del 0 al 10 y muestre por pantalla la calificación según la siguiente tabla:
- 0-2: Muy deficiente
- 3-4: Insuficiente
- 5-6: Suficiente
- 7: Bien
- 8-9: Notable
- 10: Sobresaliente
"""

note_user = int( input("Nota del 0 al 10: "))

if (note_user >= 0) and (note_user < 3):
    print("La nota {} ---> Muy deficiente".format(note_user))

elif (note_user >= 3) and (note_user < 5):
    print("La nota {} ---> Insuficiente".format(note_user))

elif (note_user >= 5) and (note_user < 7):
    print("La nota {} ---> Suficiente".format(note_user))

elif note_user == 7:
    print("La nota {} ---> Bien".format(note_user))

elif (note_user >= 8) and (note_user < 10):
    print("La nota {} ---> Notable".format(note_user))

elif note_user == 10:
    print("La nota {} ---> Sobresaliente".format(note_user))

else:
    print("Nota inválida")