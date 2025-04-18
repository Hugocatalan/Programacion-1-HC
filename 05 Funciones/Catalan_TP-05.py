import math
from colorama import Fore, Style, init

# Inicializar colorama para que los colores funcionen correctamente en consola
init(autoreset=True)

# 1. Función que imprime "Hola Mundo!"
def imprimir_hola_mundo():
    print(Fore.CYAN + "Hola Mundo!")

# 2. Función que saluda al usuario
def saludar_usuario(nombre):
    return Fore.GREEN + f"Hola {nombre}!"

# 3. Función que muestra información personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(Fore.YELLOW + f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4. Funciones para calcular área y perímetro de un círculo
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# 5. Función que convierte segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600

# 6. Función que imprime la tabla de multiplicar de un número
def tabla_multiplicar(numero):
    print(Fore.MAGENTA + f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(Fore.MAGENTA + f"{numero} x {i} = {numero * i}")

# 7. Función que realiza operaciones básicas y devuelve una tupla
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinido"
    return (suma, resta, multiplicacion, division)

# 8. Función que calcula el índice de masa corporal (IMC)
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return round(imc, 2)

# 9. Función que convierte Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 10. Función que calcula el promedio de tres números
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
if __name__ == "__main__":
    imprimir_hola_mundo()

    nombre = input(Fore.BLUE + "\n¿Tu nombre?: ")
    print(saludar_usuario(nombre))

    print(Fore.BLUE + "\nIngresá tus datos personales:")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = input("Edad: ")
    residencia = input("Residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)

    radio = float(input(Fore.BLUE + "\nIngresá el radio de un círculo: "))
    print(Fore.RED + f"Área: {calcular_area_circulo(radio):.2f}")
    print(Fore.RED + f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")

    segundos = int(input(Fore.BLUE + "\nIngresá una cantidad de segundos: "))
    print(Fore.CYAN + f"Equivale a {segundos_a_horas(segundos):.2f} horas")

    numero = int(input(Fore.BLUE + "\n¿De qué número querés la tabla de multiplicar?: "))
    tabla_multiplicar(numero)

    print(Fore.BLUE + "\nOperaciones básicas entre dos números:")
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    suma, resta, mult, div = operaciones_basicas(a, b)
    print(Fore.GREEN + f"Suma: {suma}, Resta: {resta}, Multiplicación: {mult}, División: {div}")

    peso = float(input(Fore.BLUE + "\nIngresá tu peso en kg: "))
    altura = float(input("Ingresá tu altura en metros: "))
    print(Fore.YELLOW + f"Tu IMC es: {calcular_imc(peso, altura)}")

    celsius = float(input(Fore.BLUE + "\nTemperatura en Celsius: "))
    print(Fore.CYAN + f"Equivale a {celsius_a_fahrenheit(celsius):.2f} °F")

    print(Fore.BLUE + "\nCalculando promedio de tres números:")
    n1 = float(input("Número 1: "))
    n2 = float(input("Número 2: "))
    n3 = float(input("Número 3: "))
    print(Fore.MAGENTA + f"El promedio es: {calcular_promedio(n1, n2, n3):.2f}")
    print(Fore.RED + "\n¡Programa finalizado!")
# Fin del programa