import csv
import os


total_csv_files = 0
for file in os.listdir("./csv/"):
    if file.endswith(".csv"):
        total_csv_files += 1

file_path = "./csv/products.csv"
updated_file_path = f"./csv/products_updated_{total_csv_files}.csv"

print(f"Total csv files: {total_csv_files}")
with open(file_path, mode="r") as file:
    csv_reader = csv.DictReader(file)
    # Obtener los nombres de las columnas existentes
    fieldnames = csv_reader.fieldnames + ["total_value"]

    with open(updated_file_path, mode="w", newline="") as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
        csv_writer.writeheader()

        for row in csv_reader:
            row["total_value"] = int(row["price"]) * int(row["quantity"])
            csv_writer.writerow(row)
