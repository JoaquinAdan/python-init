numbers = [1, 2, 3, 4, 5, 6]
# for i in numbers:
#     # if 0 == i % 2:
#     print(f"Aqui i es igual a: {i}")

for i in range(3, 10):
    print(f"Aqui i es igual a: {i}")

fruits = ["manzana", "cherry", "banana", "naranja"]
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        print("banana encontrada")
        # finish bucle
        break

x = 0
while x <= 5:
    if x == 3:
        break
    print(f"El valor de x es: {x}")
    x += 1

numbers2 = [1, 2, 3, 4, 5, 6]
for i in numbers2:
    if i == 3:
        continue
    print(f"Aqui i es igual a: {i}")

persons = [
    {"nombre": "Jose", "activo": True},
    {"nombre": "Maria", "activo": False},
    {"nombre": "Gerardo", "activo": True},
]

personas_activas = []
for person in persons:
    if person["activo"] == False:
        continue
    personas_activas.append(person["nombre"])

print(personas_activas)

personas_activas_comprehesion = [
    person["nombre"] for person in persons if person["activo"]
]

print(personas_activas_comprehesion)


# pelotas = ["roja", "azul", "verde", "amarilla", "roja", "roja", "verde"]
pelotas = [
    ["roja", "20cm", "redonda"],
    ["azul", "30cm", "ovalada"],
    ["verde", "40cm", "cuadrada"],
    ["amarilla", "50cm", "triangular"],
    ["roja", "60cm", "hexagonal"],
    ["roja", "70cm", "octagonal"],
    ["verde", "80cm", "redonda"],
]

claves = ["color", "tamaño", "forma"]

for caracteristicas in pelotas:
    for index, caracteristica in enumerate(caracteristicas):
        print({claves[index]: caracteristica})
    print("\n")
