import random

# Generar un numero entero aleatorio
random_number = random.randint(1, 10)
print(random_number)

# Elejir colores aleatorios
colors = ["rojo", "verde", "azul", "amarillo", "naranja"]
random_color = random.choice(colors)
print(random_color)

# Barajar una lista de cartas
cards = ["As", "Rey", "Reina", "Jota", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
random.shuffle(cards)
print(cards)

# 1. OS (Sistema Operativo):
# os.getcwd() Retorna el directorio de trabajo actual.
# os.chdir(path): Cambia el directorio de trabajo actual al especificado.
# os.listdir(path): Lista los archivos y carpetas en el directorio especificado.
# os.makedirs(path): Crea directorios de manera recursiva.
# os.remove(path): Elimina el archivo especificado.
# os.path.join(*paths): Une componentes de una ruta de manera segura según el sistema operativo.
# os.path.exists(path): Verifica si una ruta existe.
# os.rename(src, dst): Renombra un archivo o directorio.
# os.environ: Proporciona acceso a las variables de entorno del sistema.
# 2. Módulo (Operaciones Matemáticas):
# math.sqrt(x): Retorna la raíz cuadrada de x.
# math.pow(x, y): Eleva x a la potencia y (equivalente a x ** y).
# math.ceil(x): Redondea un número hacia arriba (al entero más cercano).
# math.floor(x): Redondea un número hacia abajo (al entero más cercano).
# math.factorial(x): Retorna el factorial de x.
# math.fabs(x): Retorna el valor absoluto de x (como número flotante).
# math.log(x[, base]): Retorna el logaritmo de x con base base (por defecto, base e).
# math.sin(x), math.cos(x), math.tan(x): Retorna el seno, coseno y tangente de x (en radianes).
# math.pi: Retorna el valor de π (pi).
# 3. Módulo (Generación Aleatoria):
# random.random(): Retorna un número flotante aleatorio entre 0.0 y 1.0.
# random.randint(a, b): Retorna un entero aleatorio entre a y b (ambos inclusive).
# random.choice(seq): Retorna un elemento aleatorio de una secuencia (como una lista).
# random.shuffle(seq): Baraja una secuencia (lista) en su lugar.
# random.sample(population, k): Retorna una lista de tamaño k con elementos aleatorios sin repetición de la population.
# random.uniform(a, b): Retorna un número flotante aleatorio entre a y b.
# random.gauss(mu, sigma): Retorna un número siguiendo una distribución normal (gaussiana) con media mu y desviación estándar sigma.