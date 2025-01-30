squares = [x**2 for x in range(1, 11)]
# print("Cuadrados:", squares)

celsius = [0, 10, 20, 30, 40]
fahenheit = [((9 / 5) * temp + 32) for temp in celsius]
# print("Fahenheit:", fahenheit)

evens = [x for x in range(1, 20) if x % 2 == 0]
odd = [x for x in range(1, 20) if x % 2 != 0]
# print("Pares:", evens)
# print("Impares:", odd)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# print("Matriz original:", matrix)
# print("Matriz transpuesta:", transposed)

transposed = []
for i in range(len(matrix[0])):
    # print("ejecuto primer for")
    # print("indice", i)
    transposed_row = []
    for row in matrix:
        # print("ejecuto segundo for")
        # print("row", row)
        # print("primer", transposed_row)
        transposed_row.append(row[i])
    transposed.append(transposed_row)
    # print("segundo", transposed_row)

# print("transposed", transposed)

# 1- Doble de los Números
# Dada una lista de números [1, 2, 3, 4, 5], crea una nueva lista que contenga el doble de cada número usando una List Comprehension.

numeros = [1, 2, 3, 4, 5]
doble = [x * 2 for x in numeros]
# print(doble)

# 2- Filtrar y Transformar en un Solo Paso
# Tienes una lista de palabras ["sol", "mar", "montaña", "rio", "estrella"] y quieres obtener una nueva lista con las palabras que tengan más de 3 letras y estén en mayúsculas.

palabras = ["sol", "mar", "montaña", "rio", "estrella"]
filtro_cantidad_palabras = [x for x in palabras if len(x) <= 3]
# print(filtro_cantidad_palabras)

# 3- Crear un Diccionario con List Comprehension
# Tienes dos listas, una de claves ["nombre", "edad", "ocupación"] y otra de valores ["Juan", 30, "Ingeniero"]. Crea un diccionario combinando ambas listas usando una List Comprehension.

claves = ["nombre", "edad", "ocupación", "sexo"]
valores = ["Juan", 30, "Ingeniero", "M"]
diccionario = {
    claves[i]: valores[i] if i < len(valores) else None for i in range(len(claves))
}
# print(diccionario)

# Calcula la matriz traspuesta utilizando una List Comprehension anidada.
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

traspuesta = [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]
# print(traspuesta)
suma_matriz = sum([sum(fila) for fila in matriz])
# print(suma_matriz)

# Extraer Información de una Lista de Diccionarios
# Dada una lista de diccionarios que representan personas:
personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"},
]
# Extrae una lista de nombres de personas que viven en “Madrid” y tienen más de 30 años.

personas_mayores_30 = [
    p for p in personas if p["ciudad"] == "Madrid" and p["edad"] > 30
]
nombres_personas_30 = [
    persona["nombre"] for persona in personas if persona["edad"] > 30
]
print(nombres_personas_30)
# print(personas_mayores_30)

# List Comprehension con un else
# Dada una lista de números [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], crea una nueva lista multiplicando por 2 los números pares y dejando los impares como están.

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens_x = [n * 2 if n % 2 == 0 else n for n in lista_numeros]
print(evens_x)

# multiplicados_pero_con_for = []
# for n in lista_numeros:
#     if n % 2 == 0:
#         multiplicados_pero_con_for.append(n * 2)
#     else:
#         multiplicados_pero_con_for.append(n)
# print(multiplicados_pero_con_for)
