class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - Cantidad: {self.cantidad}, Precio:{self.precio}"

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto {producto.nombre} agregado.")

    def eliminar_producto(self, nombre):
        self.productos = [p for p in self.productos if p.nombre != nombre]
        print(f"Producto {nombre} eliminado si existia.")

    def actualizar_producto(self, nombre, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.nombre == nombre:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                print(f"Producto {nombre} actualizado.")
                return
        print(f"Producto {nombre} no encontrado.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario esta vacio")
        else:
            print("\nInventario")
            for producto in self.productos:
                print(producto)

#Ejemplos de uso
inv = Inventario()
p1 = Producto("Laptop", 10, 800)
p2 = Producto("PS5Pro", 15, 1000)
p3 = Producto("Mouse", 20, 15)

inv.agregar_producto(p1)
inv.agregar_producto(p2)
inv.mostrar_inventario()
inv.actualizar_producto("PS5Pro", 5, 1100)
inv.eliminar_producto("Laptop")
inv.agregar_producto(p3)
inv.mostrar_inventario()
