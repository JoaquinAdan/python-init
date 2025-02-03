import csv

new_product = {
    "name": "Wireless charger",
    "price": 75,
    "quantity": 10,
    "brand": "Samsung",
    "category": "Accessories",
    "entry_date": "2021-08-01",
}

with open("./csv/products.csv", mode="a", newline="") as file:
    csv_writer = csv.DictWriter(file, fieldnames=new_product.keys())
    csv_writer.writerow(new_product)
