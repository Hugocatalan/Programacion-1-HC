# Actividad 1:
for i in range(101):
    print(i)

# Actividad 2: 
numero = input("Ingresa un número entero: ")
print("Cantidad de dígitos:", len(numero.strip('-')))

# Actividad 3: 
inicio = int(input("Ingresa el primer número: "))
fin = int(input("Ingresa el segundo número: "))
suma = 0
for i in range(min(inicio, fin) + 1, max(inicio, fin)):
    suma += i
print("La suma es:", suma)

# Actividad 4: 
suma = 0
while True:
    numero = int(input("Ingresa un número (0 para salir): "))
    if numero == 0:
        break
    suma += numero
print("Suma total:", suma)

# Actividad 5:
import random
numero_secreto = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivina el número (0-9): "))
    intentos += 1
    if intento == numero_secreto:
        print(f"¡Correcto! Lo adivinaste en {intentos} intento(s).")
        break

# Actividad 6: 
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

# Actividad 7: 
limite = int(input("Ingresa un número entero positivo: "))
suma = sum(range(limite + 1))
print("Suma total:", suma)

# Actividad 8: 
cantidad = 100
pares = impares = positivos = negativos = 0
for _ in range(cantidad):
    numero = int(input("Ingresa un número: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero >= 0:
        positivos += 1
    else:
        negativos += 1
print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

# Actividad 9: 
cantidad = 100
suma = 0
for _ in range(cantidad):
    numero = int(input("Ingresa un número: "))
    suma += numero
print("Media:", suma / cantidad)

# Actividad 10: 
numero = input("Ingresa un número entero: ")
numero_invertido = numero[::-1] if not numero.startswith('-') else '-' + numero[:0:-1]
print("Número invertido:", numero_invertido)
