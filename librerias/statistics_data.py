import statistics
import csv

# Leer los datos de ventas mensuales desde un archivo CSV
monthly_sales = {}
with open('./librerias/monthly_sales.csv', mode='r') as file:
  reader = csv.DictReader(file)
  for row in reader:
    month = row['month']
    sales = int(row['sales'])
    monthly_sales[month] = sales
    
sales = list(monthly_sales.values())
print(sales)

# Hallar la media
mean_sales = statistics.mean(sales)
print(f"La media anual es: {mean_sales}")

# Hallar la mediana
median_sales = statistics.median(sales)
print(f"La mediana anual es: {median_sales}")

# Hallar la moda
mode_sales = statistics.mode(sales)
print(f"La moda anual es: {mode_sales}")

# Desviación estándar
stddev_sales = statistics.stdev(sales)
print(f"La desviación estándar anual es: {stddev_sales}")

# Hallar la varianza
variance_sales = statistics.variance(sales)
print(f"La varianza anual es: {variance_sales}")

max_sales = max(sales)
min_sales = min(sales)

range_sales = max_sales - min_sales

print(f"El rango anual es: {range_sales}")
