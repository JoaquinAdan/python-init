import reports

# Generar reportes de ventas y gastos usando funciones del módulo reports

sales_report = reports.generate_sales_report("June", 10000)
expense_report = reports.generate_expense_report("Octubre", 5000)

print(sales_report)
print(expense_report)
