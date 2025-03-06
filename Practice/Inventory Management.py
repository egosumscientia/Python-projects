from Scripts.activate_this import prev_length

inventario = []

def agregar_producto(nombre, cantidad, precio):
    producto = {"nombre":nombre, "cantidad":cantidad, "precio":precio}
    inventario.append(producto)
    print(f"Producto {nombre} agregado.")

def eliminar_producto(nombre):
    global inventario
    inventario = [producto for producto in inventario if producto["nombre"] != nombre]
    print(f"Producto {nombre} eliminado si existia")

def actualizar_producto(nombre, cantidad=None, precio=None):
    for producto in inventario:
        if producto["nombre"] == nombre:
            if cantidad is not None:
                producto["cantidad"] = cantidad
            if precio is not None:
                producto["precio"] = precio
            print(f"Producto {nombre} actualizado")
            return
    print(f"Producto {nombre} no encontrado.")

def mostrar_inventario():
    if not inventario:
        print("El inventario esta vacio")
    else:
        print("\nInventario")
        for producto in inventario:
            print(f"Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio:{producto['precio']}")

agregar_producto("Laptop", 10, 800)
agregar_producto("Mouse", 50, 25)
mostrar_inventario()
actualizar_producto("Mouse", cantidad=45)
eliminar_producto("Laptop")
agregar_producto("Monitor", 40, 34)
mostrar_inventario()