 #Ejercicio 1 ////////////
def factorial(n):
    if n == 0 or n == 1:
        return 1  #Caso base
    else:
        return n * factorial(n - 1) # Caso recursivo
    
limite = int(input("Ingrese un numero positivo que se utilizara como limite: ")) 
   
print("Los factoriales del 0 al limite ingresado son:")
for l in range(limite + 1):
    print(f"El factorial de {l} es: {factorial(l)}")   

    
    
 #Ejercicio 2 ////////////
def fibonacci(n):
    if n == 0:
        return 0  #Caso base
    elif n == 1:
        return 1  #Caso base
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) # Caso recursivo
    
posicion = int(input("Ingrese la posicion del numero de Fibonacci que desea calcular: "))
print(f"El numero de Fibonacci en la posicion {posicion} es: {fibonacci(posicion)}")       


#Ejercicio 3 ////////////

def potencia(base, exponente):
    if exponente == 0:
        return 1  #Caso base
    else:
        return base * potencia(base, exponente - 1) # Caso recursivo
    
base = int(input("Ingrese el número base: ")) 
exponente = int(input("Ingrese el número exponente: "))  

resultado = potencia(base, exponente)
print(f"El resultado de {base} elevado a la potencia {exponente} es: {resultado}")


#Ejercicio 4 ////////////

def decimal_a_binario(n):
    if n == 0:
        return "0"  #Caso base
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2) # Caso recursivo
    
numero = int(input("Ingresa un numero entero positivo: "))

if numero < 0:
    print("El número debe ser positivo.")
else:
    resultado = decimal_a_binario(numero)
    print(f"El número {numero} en binario es: {resultado}")
    
      
#Ejercicio 5 ////////////
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True  #Caso base
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])
    
palabra = input("Ingrese una palabra o frase: ").replace(" ", "").lower() 
if es_palindromo(palabra):
    print(f"La palabra o frase '{palabra}' es un palíndromo.")
else:
    print(f"La palabra o frase '{palabra}' no es un palíndromo.")
    
   
#Ejercicio 6 ////////////

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)
numero = int(input("Ingrese un número entero positivo: "))
if numero < 0:
    print("El número debe ser positivo.")
else:
    resultado = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es: {resultado}")
 
    
#Ejercicio 7 ////////////
def contador_bloques(n):
    if n == 1:
        return 1  #Caso base
    else:
        return n + contador_bloques(n - 1) # Caso recursivo
n = int(input("Ingrese el número de bloques: "))
if n < 1:
    print("El número de bloques debe ser positivo.")
    
contador_bloques(n)
print(f"El número total de bloques es: {contador_bloques(n)}")    
   
   
#Ejercicio 8 ////////////
def contador_digitos(numero,digito):
    if numero == 0:
        return 0  #Caso base
    else:
        cuenta = 1 if (numero % 10) == digito else 0
        return cuenta + contador_digitos(numero // 10, digito)
    
numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese el dígito que desea contar: "))
if numero < 0 or digito < 0 or digito > 9:
    print("El número y el dígito deben ser positivos.")    
    
contador_digitos(numero,digito)
print(f"El dígito {digito} aparece {contador_digitos(numero,digito)} veces en el número {numero}.")


