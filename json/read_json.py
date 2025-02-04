import json

# Lectura del archivo
with open("./json/product.json", mode="r") as file:
    products = json.load(file)

# Mostrar el contenido
for product in products:
    # print(product)
    print(f"Producto: {product['name']}, Precio: {product['price']}")
