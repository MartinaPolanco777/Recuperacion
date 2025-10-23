# Programa: Recolección de datos de clientes y productos
# Autor: (Martina polanco)
# Descripción: Simula la recolección de datos de un cliente y sus productos.

# Solicitar datos del cliente
nombre_cliente = input("Ingrese el nombre del cliente: ")
correo_cliente = input("Ingrese el correo del cliente: ")
telefono_cliente = input("Ingrese el telefono del cliente: ")

# Crear una lista para guardar los productos
productos = []

# Pedir cantidad de productos a registrar
cantidad_productos = int(input("¿Cuántos productos desea registrar?: "))

for i in range(cantidad_productos):
    print(f"\nProducto {i+1}:")
    nombre_producto = input("Nombre del producto: ")
    
    # Validar que el precio sea positivo
    precio = float(input("Precio del producto: "))
    if precio <= 0:
        print("⚠ El precio debe ser un numero positivo. Se establecera en 0.")
        precio = 0
    
    # Validar que la cantidad sea valida (entero positivo)
    cantidad = int(input("Cantidad disponible: "))
    if cantidad < 0:
        print("⚠ La cantidad no puede ser negativa. Se establecera en 0.")
        cantidad = 0
    
    # Guardar producto en un diccionario
    producto = {
        "nombre": nombre_producto,
        "precio": precio,
        "cantidad": cantidad
    }
    productos.append(producto)

# Mostrar los datos ingresados
print("\n=== INFORMACION DEL CLIENTE ===")
print(f"Nombre: {nombre_cliente}")
print(f"Correo: {correo_cliente}")
print(f"Telefono: {telefono_cliente}")

print("\n=== PRODUCTOS REGISTRADOS ===")
for p in productos:
    print(f"- {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

#EXPLICACION CODIGO

"""Este programa simula la recolección de datos de un cliente y sus productos
sin usar una base de datos.

El usuario ingresa la información del cliente (nombre, correo y teléfono),
y luego los datos de los productos (nombre, precio y cantidad).

Se utilizan estructuras condicionales "if" para validar que:
- El precio sea un número positivo.
- La cantidad de productos no sea negativa.

Al final, el programa muestra toda la información ingresada
de forma organizada y legible en pantalla."""