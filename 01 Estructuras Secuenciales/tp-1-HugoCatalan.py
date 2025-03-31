# 1) Imprimir "Hola Mundo!"
print("Hola Mundo!")

# 2) Pedir el nombre al usuario y saludarlo
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# 3) Pedir nombre, apellido, edad y residencia, e imprimir una oración
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4) Calcular el área y perímetro de un círculo
import math
radio = float(input("Ingrese el radio del círculo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"Área: {area:.2f}, Perímetro: {perimetro:.2f}")

# 5) Convertir segundos a horas
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos / 3600
print(f"Equivale a {horas:.2f} horas")

# 6) Imprimir la tabla de multiplicar de un número
tabla = int(input("Ingrese un número: "))
for i in range(1, 11):
    print(f"{tabla} x {i} = {tabla * i}")

# 7) Operaciones con dos números enteros distintos de 0
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
if num1 != 0 and num2 != 0:
    print(f"Suma: {num1 + num2}")
    print(f"Resta: {num1 - num2}")
    print(f"Multiplicación: {num1 * num2}")
    print(f"División: {num1 / num2:.2f}")
else:
    print("Los números no pueden ser 0.")

# 8) Calcular el Índice de Masa Corporal (IMC)
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
print(f"Su IMC es: {imc:.2f}")

# 9) Convertir Celsius a Fahrenheit
temp_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
temp_fahrenheit = (9/5) * temp_celsius + 32
print(f"Temperatura en Fahrenheit: {temp_fahrenheit:.2f}")

# 10) Calcular el promedio de tres números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio es: {promedio:.2f}")
HugoH