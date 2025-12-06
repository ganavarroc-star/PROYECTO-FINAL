"""
Pruebas Unitarias para la estructura de Árbol Binario de Búsqueda
y el Gestor de Inventario
"""

import unittest
from arbol_binario import ArbolBinarioBusqueda, Nodo
from main import GestorInventario


class TestArbolBinarioBusqueda(unittest.TestCase):
    """Pruebas para la clase ArbolBinarioBusqueda"""
    
    def setUp(self):
        """Configura un árbol vacío para cada prueba"""
        self.arbol = ArbolBinarioBusqueda()
    
    def test_arbol_vacio(self):
        """Verifica que un árbol recién creado está vacío"""
        self.assertIsNone(self.arbol.raiz)
        self.assertEqual(len(self.arbol.recorrido_inorden()), 0)
    
    def test_insertar_un_elemento(self):
        """Verifica la inserción de un elemento"""
        self.arbol.insertar(5, "Producto A", 10, 25.50)
        self.assertIsNotNone(self.arbol.raiz)
        self.assertEqual(self.arbol.raiz.producto_id, 5)
    
    def test_insertar_multiples_elementos(self):
        """Verifica la inserción de múltiples elementos"""
        self.arbol.insertar(10, "Producto A", 5, 50.0)
        self.arbol.insertar(5, "Producto B", 3, 30.0)
        self.arbol.insertar(15, "Producto C", 2, 75.0)
        self.assertEqual(len(self.arbol.recorrido_inorden()), 3)
    
    def test_buscar_elemento_existente(self):
        """Verifica la búsqueda de un elemento existente"""
        self.arbol.insertar(10, "Producto A", 5, 50.0)
        self.arbol.insertar(5, "Producto B", 3, 30.0)
        
        resultado = self.arbol.buscar(5)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.nombre, "Producto B")
    
    def test_buscar_elemento_no_existente(self):
        """Verifica la búsqueda de un elemento que no existe"""
        self.arbol.insertar(10, "Producto A", 5, 50.0)
        resultado = self.arbol.buscar(999)
        self.assertIsNone(resultado)
    
    def test_eliminar_hoja(self):
        """Verifica la eliminación de un nodo hoja"""
        self.arbol.insertar(10, "Producto A", 5, 50.0)
        self.arbol.insertar(5, "Producto B", 3, 30.0)
        self.arbol.insertar(15, "Producto C", 2, 75.0)
        
        self.arbol.eliminar(5)
        self.assertIsNone(self.arbol.buscar(5))
        self.assertEqual(len(self.arbol.recorrido_inorden()), 2)
    
    def test_eliminar_nodo_con_dos_hijos(self):
        """Verifica la eliminación de un nodo con dos hijos"""
        self.arbol.insertar(10, "Producto A", 5, 50.0)
        self.arbol.insertar(5, "Producto B", 3, 30.0)
        self.arbol.insertar(15, "Producto C", 2, 75.0)
        
        self.arbol.eliminar(10)
        self.assertIsNone(self.arbol.buscar(10))
        self.assertEqual(len(self.arbol.recorrido_inorden()), 2)
    
    def test_recorrido_inorden(self):
        """Verifica que el recorrido inorden retorna elementos ordenados"""
        self.arbol.insertar(10, "Producto A", 5, 50.0)
        self.arbol.insertar(5, "Producto B", 3, 30.0)
        self.arbol.insertar(15, "Producto C", 2, 75.0)
        self.arbol.insertar(3, "Producto D", 1, 15.0)
        self.arbol.insertar(7, "Producto E", 2, 35.0)
        
        productos = self.arbol.recorrido_inorden()
        ids = [p.producto_id for p in productos]
        self.assertEqual(ids, [3, 5, 7, 10, 15])
    
    def test_actualizar_cantidad(self):
        """Verifica la actualización de cantidad de un producto"""
        self.arbol.insertar(10, "Producto A", 5, 50.0)
        
        resultado = self.arbol.actualizar_cantidad(10, 20)
        self.assertTrue(resultado)
        
        producto = self.arbol.buscar(10)
        self.assertEqual(producto.cantidad, 20)
    
    def test_obtener_valor_total(self):
        """Verifica el cálculo del valor total del inventario"""
        self.arbol.insertar(10, "Producto A", 5, 50.0)
        self.arbol.insertar(5, "Producto B", 3, 30.0)
        self.arbol.insertar(15, "Producto C", 2, 75.0)
        
        # Valor total: (5*50) + (3*30) + (2*75) = 250 + 90 + 150 = 490
        valor_total = self.arbol.obtener_valor_total()
        self.assertEqual(valor_total, 490.0)


class TestGestorInventario(unittest.TestCase):
    """Pruebas para la clase GestorInventario"""
    
    def setUp(self):
        """Configura un gestor nuevo para cada prueba"""
        self.gestor = GestorInventario()
    
    def test_agregar_producto(self):
        """Verifica la adición de un producto"""
        resultado = self.gestor.agregar_producto(1, "Laptop", 5, 999.99)
        self.assertTrue(resultado)
        
        producto = self.gestor.arbol.buscar(1)
        self.assertIsNotNone(producto)
        self.assertEqual(producto.nombre, "Laptop")
    
    def test_agregar_producto_duplicado(self):
        """Verifica que no se permite agregar un producto con ID duplicado"""
        self.gestor.agregar_producto(1, "Laptop", 5, 999.99)
        resultado = self.gestor.agregar_producto(1, "Tablet", 3, 499.99)
        self.assertFalse(resultado)
    
    def test_buscar_producto(self):
        """Verifica la búsqueda de un producto"""
        self.gestor.agregar_producto(1, "Laptop", 5, 999.99)
        producto = self.gestor.buscar_producto(1)
        self.assertIsNotNone(producto)
        self.assertEqual(producto.nombre, "Laptop")
    
    def test_eliminar_producto(self):
        """Verifica la eliminación de un producto"""
        self.gestor.agregar_producto(1, "Laptop", 5, 999.99)
        resultado = self.gestor.eliminar_producto(1)
        self.assertTrue(resultado)
        
        producto = self.gestor.arbol.buscar(1)
        self.assertIsNone(producto)
    
    def test_actualizar_stock(self):
        """Verifica la actualización de stock"""
        self.gestor.agregar_producto(1, "Laptop", 5, 999.99)
        resultado = self.gestor.actualizar_stock(1, 10)
        self.assertTrue(resultado)
        
        producto = self.gestor.arbol.buscar(1)
        self.assertEqual(producto.cantidad, 10)
    
    def test_flujo_completo(self):
        """Verifica un flujo completo de operaciones"""
        # Agregar productos
        self.gestor.agregar_producto(101, "Laptop", 5, 999.99)
        self.gestor.agregar_producto(102, "Mouse", 15, 29.99)
        self.gestor.agregar_producto(103, "Monitor", 3, 299.99)
        
        # Verificar que existen
        self.assertIsNotNone(self.gestor.buscar_producto(101))
        self.assertIsNotNone(self.gestor.buscar_producto(102))
        self.assertIsNotNone(self.gestor.buscar_producto(103))
        
        # Actualizar stock
        self.gestor.actualizar_stock(101, 3)
        self.assertEqual(self.gestor.arbol.buscar(101).cantidad, 3)
        
        # Eliminar un producto
        self.gestor.eliminar_producto(102)
        self.assertIsNone(self.gestor.arbol.buscar(102))
        
        # Verificar que quedan 2 productos
        productos = self.gestor.arbol.recorrido_inorden()
        self.assertEqual(len(productos), 2)


if __name__ == "__main__":
    # Ejecutar las pruebas con verbosidad
    unittest.main(verbosity=2)
