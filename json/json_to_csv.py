import json
import csv

json_path = "./json/product.json"
csv_path = "./json/products.csv"

fieldnames = []


def json_to_csv(json_path, csv_path):
    with open(json_path, mode="r") as file:
        products = json.load(file)
        for product in products:
            for key in product.keys():
                if key not in fieldnames:
                    fieldnames.append(key)

        with open(csv_path, mode="w", newline="") as updated_file:
            csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            for row in products:
                csv_writer.writerow(row)


json_to_csv(json_path, csv_path)

json_path2 = "./json/product2.json"

def csv_to_json(csv_path, json_path):
    data = []
    with open(csv_path, mode="r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
        with open(json_path, mode="w") as file:
            json.dump(data, file, indent=4)


csv_to_json(csv_path, json_path2)
