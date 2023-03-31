'''
9. Calificación de un examen. Ingrese la puntuación de un examen.
Si es >= 90 La calificación es A, 
si es >= 80 La calificación es B,
si es >= 70 La calificación es C,
si >= 60 La calificación es D,
sino La calificación es F,

'''

nota = int( input("Nota: "))

if nota >= 90:
    print("La calificación es A")
elif nota >= 80:
    print("La calificación es B")
elif nota >= 70:
    print("La calificación es C")
elif nota >= 60:
    print("La calificación es D")
else:
    print("La calificación es F")  