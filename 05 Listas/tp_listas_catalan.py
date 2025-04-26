# Actividades con Listas

# 1) Lista de múltiplos de 4 del 1 al 100
multiplos_de_4 = list(range(4, 101, 4))# incluye el 4, excluye el 100 y salta de 4 en 4
print("1) Múltiplos de 4:", multiplos_de_4)

# 2) Lista de cinco elementos y mostrar el penúltimo
cosas_favoritas = ["tp", "autoevaluacion", "alumno", "UTN", "programacion"]
print("2) Penúltimo elemento:", cosas_favoritas[-2])

# 3) Lista vacía, agregar tres palabras y mostrar
lista_vacia = []
lista_vacia.append("Programacion")
lista_vacia.append("Comision11")
lista_vacia.append("Grupo2")
print("3) Lista con palabras:", lista_vacia)

# 4) Reemplazar segundo y último valor en "animales"
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print("4) Lista animales modificada:", animales)

# 5) Análisis del programa
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print("5) Lista sin el máximo:", numeros)

# 6) Lista de 10 a 30 saltando de 5 en 5 y mostrar dos primeros
numeros_saltados = list(range(10, 31, 5))
print("6) Dos primeros elementos:", numeros_saltados[0:2])

# 7) Reemplazar valores centrales en "autos"
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "mustang"
autos[2] = "camaro" 
#autos[-2] = "camaro"    en este caso  podria usar el -2 y daria el mismo resultado
print("7) Lista autos modificada:", autos)

# 8) Crear "dobles" y agregar el doble de 5, 10 y 15
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("8) Lista de dobles:", dobles)

# 9) Modificaciones en la lista "compras"
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")        # a) Agregar "jugo" al tercer cliente
compras[1][1] = "tallarines"     # b) Reemplazar "fideos" por "tallarines"
compras[0].remove("pan")          # c) Eliminar "pan"
print("9) Lista compras modificada:", compras)

# 10) Crear "lista_anidada" con elementos dados
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print("10) Lista anidada:", lista_anidada)
