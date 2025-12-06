"""
Aplicación de Gestión de Inventario
Utiliza un Árbol Binario de Búsqueda para almacenar y manipular productos.
"""

from arbol_binario import ArbolBinarioBusqueda


class GestorInventario:
    """Gestor de inventario que utiliza BST como estructura de datos central"""
    
    def __init__(self):
        self.arbol = ArbolBinarioBusqueda()
    
    def agregar_producto(self, producto_id, nombre, cantidad, precio):
        """Agrega un nuevo producto al inventario"""
        producto_existente = self.arbol.buscar(producto_id)
        if producto_existente:
            print(f"⚠️  Producto con ID {producto_id} ya existe.")
            return False
        
        self.arbol.insertar(producto_id, nombre, cantidad, precio)
        print(f"✅ Producto '{nombre}' (ID: {producto_id}) agregado al inventario.")
        return True
    
    def buscar_producto(self, producto_id):
        """Busca un producto por ID"""
        producto = self.arbol.buscar(producto_id)
        if producto:
            print(f"🔍 Producto encontrado: {producto}")
            return producto
        else:
            print(f"❌ Producto con ID {producto_id} no encontrado.")
            return None
    
    def eliminar_producto(self, producto_id):
        """Elimina un producto del inventario"""
        producto = self.arbol.buscar(producto_id)
        if producto:
            self.arbol.eliminar(producto_id)
            print(f"🗑️  Producto '{producto.nombre}' (ID: {producto_id}) eliminado.")
            return True
        else:
            print(f"❌ Producto con ID {producto_id} no encontrado para eliminar.")
            return False
    
    def actualizar_stock(self, producto_id, nueva_cantidad):
        """Actualiza la cantidad de stock de un producto"""
        if self.arbol.actualizar_cantidad(producto_id, nueva_cantidad):
            print(f"📦 Stock del producto ID {producto_id} actualizado a {nueva_cantidad} unidades.")
            return True
        else:
            print(f"❌ No se pudo actualizar el producto con ID {producto_id}.")
            return False
    
    def listar_inventario(self):
        """Lista todos los productos en orden (usando recorrido inorden)"""
        productos = self.arbol.recorrido_inorden()
        if not productos:
            print("📋 El inventario está vacío.")
            return
        
        print("\n" + "="*70)
        print("📋 INVENTARIO ACTUAL (Ordenado por ID de Producto)")
        print("="*70)
        for producto in productos:
            valor_total = producto.cantidad * producto.precio
            print(f"ID: {producto.producto_id:4} | Nombre: {producto.nombre:20} | Stock: {producto.cantidad:3} | "
                  f"Precio: ${producto.precio:8.2f} | Valor Total: ${valor_total:10.2f}")
        print("="*70)
    
    def obtener_reporte(self):
        """Genera un reporte del inventario"""
        productos = self.arbol.recorrido_inorden()
        cantidad_productos = len(productos)
        valor_total = self.arbol.obtener_valor_total()
        
        print("\n" + "="*70)
        print("📊 REPORTE DE INVENTARIO")
        print("="*70)
        print(f"Total de Productos en el Sistema: {cantidad_productos}")
        print(f"Valor Total del Inventario: ${valor_total:,.2f}")
        
        if cantidad_productos > 0:
            stock_total = sum(p.cantidad for p in productos)
            print(f"Cantidad Total de Unidades en Stock: {stock_total}")
        print("="*70 + "\n")


def main():
    """Función principal que demuestra la funcionalidad del gestor de inventario"""
    
    print("\n🚀 Sistema de Gestión de Inventario con Árbol Binario de Búsqueda")
    print("="*70 + "\n")
    
    gestor = GestorInventario()
    
    # Agregar productos de prueba
    print("📥 AGREGANDO PRODUCTOS AL INVENTARIO:\n")
    gestor.agregar_producto(101, "Laptop", 5, 999.99)
    gestor.agregar_producto(50, "Mouse", 15, 29.99)
    gestor.agregar_producto(150, "Monitor", 3, 299.99)
    gestor.agregar_producto(75, "Teclado", 8, 79.99)
    gestor.agregar_producto(25, "Hub USB", 12, 49.99)
    gestor.agregar_producto(200, "Webcam", 4, 89.99)
    
    # Listar inventario
    print("\n")
    gestor.listar_inventario()
    
    # Buscar producto
    print("\n🔍 BÚSQUEDA DE PRODUCTOS:\n")
    gestor.buscar_producto(101)
    gestor.buscar_producto(500)  # No existe
    
    # Actualizar stock
    print("\n📦 ACTUALIZANDO STOCK:\n")
    gestor.actualizar_stock(101, 3)
    gestor.actualizar_stock(50, 20)
    
    # Listar inventario actualizado
    print("\n")
    gestor.listar_inventario()
    
    # Eliminar producto
    print("\n🗑️  ELIMINANDO PRODUCTO:\n")
    gestor.eliminar_producto(25)
    
    # Listar inventario final
    print("\n")
    gestor.listar_inventario()
    
    # Reporte final
    gestor.obtener_reporte()
    
    print("✨ Demostración completada. La estructura de datos BST funcionó correctamente.")


if __name__ == "__main__":
    main()
