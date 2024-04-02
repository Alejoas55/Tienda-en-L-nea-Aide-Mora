print("Bienvenido a la Tienda Virtual Aide Mora")

class Catalogo:
    _solicitud = None

    def solicitud():
        if Catalogo._solicitud is None:
            Catalogo._solicitud = Catalogo()
        return Catalogo._solicitud

    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

class Producto:
    def __init__(self, nombre, descripcion, precio, categoria):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.categoria = categoria

class Carro:
    def __init__(self):
        self.items = []

    def agregar_item(self, producto, cantidad):
        self.items.append({"producto": producto, "cantidad": cantidad})

    def calcular_total(self):
        return sum(item["producto"].precio * item["cantidad"] for item in self.items)

class MenuPrincipal:
    def __init__(self):
        self.catalogo = Catalogo.solicitud()
        self.carro = Carro()

    def mostrar_menu(self):
        print("Menú:")
        print("1. Ver productos disponibles")
        print("2. Ver detalles de un producto")
        print("3. Agregar producto al carro")
        print("4. Ver carro de compras")
        print("5. Realizar pedido")
        print("6. Salir")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.mostrar_productos()
            elif opcion == "2":
                self.mostrar_detalles_producto()
            elif opcion == "3":
                self.agregar_al_carro()
            elif opcion == "4":
                self.mostrar_carro()
            elif opcion == "5":
                self.realizar_pedido()
            elif opcion == "6":
                print("Gracias por utilizar nuestra tienda en línea Aide Mora")
                break
            else:
                print("Opción no válida.Seleccione una opción válida.")

    def mostrar_productos(self):
        print("Productos disponibles:")
        for producto in self.catalogo.productos:
            print(f"{producto.nombre} - ${producto.precio} Pesos")

    def mostrar_detalles_producto(self):
        nombre_producto = input("Ingrese el nombre del producto: ")
        for producto in self.catalogo.productos:
            if producto.nombre == nombre_producto:
                print(f"Nombre: {producto.nombre}")
                print(f"Descripción: {producto.descripcion}")
                print(f"Precio: ${producto.precio} Pesos")
                print(f"Categoría: {producto.categoria}")
                return
        print("Producto no encontrado.")

    def agregar_al_carro(self):
        nombre_producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad: "))
        for producto in self.catalogo.productos:
            if producto.nombre == nombre_producto:
                self.carro.agregar_item(producto, cantidad)
                print("Producto agregado al carro.")
                return
        print("Producto no encontrado.")

    def mostrar_carro(self):
        print("Carro de compras:")
        for item in self.carro.items:
            print(f"{item['producto'].nombre} - Cantidad: {item['cantidad']} - Subtotal: ${item['producto'].precio * item['cantidad']} Pesos")
        print(f"Total a pagar: ${self.carro.calcular_total()} Pesos")

    def realizar_pedido(self):
        print("Realizar pedido:")
        print("Pedido realizado.")

if __name__ == "__main__":
    catalogo = Catalogo.solicitud()
    catalogo.agregar_producto(Producto("Camiseta", "Camiseta", 20000, "Ropa"))
    catalogo.agregar_producto(Producto("Jeans", "Jeans", 40000, "Ropa"))
    catalogo.agregar_producto(Producto("Zapatos", "Zapatos", 60000, "Calzado"))
    catalogo.agregar_producto(Producto("Tenis", "Tenis", 70000, "Calzado"))
    catalogo.agregar_producto(Producto("Buso", "Buso", 60000, "Ropa"))
    catalogo.agregar_producto(Producto("Medias", "Medias", 10000, "Ropa"))
    catalogo.agregar_producto(Producto("Chaqueta", "Chaqueta", 100000, "Ropa"))

    interfaz = MenuPrincipal()
    interfaz.ejecutar()