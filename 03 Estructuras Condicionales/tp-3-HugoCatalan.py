# Actividad 1
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")


# Actividad 2
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# Actividad 3
numero = int(input("Ingrese un número par: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


# Actividad 4
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif 12 <= edad < 18:
    print("Adolescente")
elif 18 <= edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# Actividad 5
contrasena = input("Ingrese una contraseña (entre 8 y 14 caracteres): ")
if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# Actividad 6
from statistics import mode, median, mean, StatisticsError
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print("Lista de números aleatorios:")
print(numeros_aleatorios)
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
try:
    moda = mode(numeros_aleatorios)
except StatisticsError:
    print("No hay una única moda en la lista.")
    moda = None
print(f"\nMedia: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
if moda is not None:
    if media > mediana and mediana > moda:
        print("\nDistribución con sesgo positivo (a la derecha).")
    elif media < mediana and mediana < moda:
        print("\nDistribución con sesgo negativo (a la izquierda).")
    elif media == mediana == moda:
        print("\nDistribución sin sesgo.")
    else:
        print("\nDistribución sin un sesgo claro (no cumple las condiciones estrictas).")



# Actividad 7
texto = input("Ingresá una frase o palabra: ")
if texto[-1].lower() in 'aeiou':
    texto += "!"
print("Resultado:", texto)


# Actividad 8
nombre = input("Ingresá tu nombre: ")
print("Elegí una opción:")
print("1 - Nombre en MAYÚSCULAS")
print("2 - Nombre en minúsculas")
print("3 - Nombre con la primera letra en mayúscula")
opcion = input("Ingresá 1, 2 o 3 según lo que quieras: ")
if opcion == "1":
    resultado = nombre.upper()
elif opcion == "2":
    resultado = nombre.lower()
elif opcion == "3":
    resultado = nombre.title()
else:
    resultado = "Opción no válida."
print("Resultado:", resultado)


# Actividad 9
magnitud = float(input("Ingresá la magnitud del terremoto (escala de Richter): "))
if magnitud < 3:
    resultado = "Muy leve (imperceptible)"
elif magnitud >= 3 and magnitud < 4:
    resultado = "Leve (ligeramente perceptible)"
elif magnitud >= 4 and magnitud < 5:
    resultado = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif magnitud >= 5 and magnitud < 6:
    resultado = "Fuerte (puede causar daños en estructuras débiles)"
elif magnitud >= 6 and magnitud < 7:
    resultado = "Muy Fuerte (puede causar daños significativos)"
else:  
    resultado = "Extremo (puede causar graves daños a gran escala)"
print("Clasificación:", resultado)

# Actividad 10
hemisferio = input("¿En qué hemisferio estás? (N para Norte / S para Sur): ").upper()
mes = int(input("Ingresá el número del mes (1 al 12): "))
dia = int(input("Ingresá el día del mes: "))
fecha = (mes, dia)
if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Otoño"
    else:
        estacion = "Fecha inválida"

elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Primavera"
    else:
        estacion = "Fecha inválida"
else:
    estacion = "Hemisferio no reconocido."
print("La estación es:", estacion)


