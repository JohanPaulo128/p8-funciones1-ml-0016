print("Johan Paulo Aros Reveles NC 0016")
print("Sintaxis básica de una función en Python, Ejemplo 1")
def saludar():
    print("¡Hola, mundo!")

# Llamar a la función
saludar()
# Salida: ¡Hola, mundo!

print("Anatomía de una función, Ejemplo2")
def nombre_funcion(parametro1, parametro2):  # 1. Definición
    """Docstring: descripción de la función"""  # 2. Documentación (opcional)
    # 3. Cuerpo de la función (indentado)
    resultado = parametro1 + parametro2
    return resultado  # 4. Retorno (opcional)

print("Parámetros posicionales, Ejemplo 3")
def calcular_area_rectangulo(ancho, alto):
    """Calcula el área de un rectángulo"""
    area = ancho * alto
    return area

# Llamar a la función
resultado = calcular_area_rectangulo(5, 10)
print(resultado)  # Salida: 50

# El orden importa
resultado2 = calcular_area_rectangulo(10, 5)
print(resultado2)  # Salida: 50 (mismo resultado en este caso)

print ("Parámetros con nombre (keyword arguments),Ejemplo 4")
def crear_usuario(nombre, edad, ciudad):
    return f"{nombre}, {edad} años, de {ciudad}"

# Usando parámetros posicionales
usuario1 = crear_usuario("Ana", 25, "Madrid")

# Usando parámetros con nombre (más claro)
usuario2 = crear_usuario(nombre="Carlos", edad=30, ciudad="Barcelona")

# Puedes cambiar el orden si usas nombres
usuario3 = crear_usuario(ciudad="Valencia", nombre="Laura", edad=28)

print(usuario1)  # Ana, 25 años, de Madrid
print(usuario2)  # Carlos, 30 años, de Barcelona
print(usuario3)  # Laura, 28 años, de Valencia

print("Parámetros con valores por defecto, Ejemplo5")
def saludar(nombre, saludo="Hola"):
    """Saluda a una persona con un saludo personalizable"""
    return f"{saludo}, {nombre}!"

print(saludar("María"))  # Hola, María!
print(saludar("Pedro", "Buenos días"))  # Buenos días, Pedro!
print(saludar("Ana", saludo="Qué tal"))  # Qué tal, Ana!

print("Johan Paulo Aros Reveles NC 0016")