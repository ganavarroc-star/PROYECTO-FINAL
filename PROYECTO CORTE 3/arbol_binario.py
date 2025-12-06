"""
Módulo de Árbol Binario de Búsqueda (BST)
Proporciona la estructura de datos central para el sistema de inventario.
"""

class Nodo:
    """Representa un nodo en el árbol binario de búsqueda"""
    
    def __init__(self, producto_id, nombre, cantidad, precio):
        self.producto_id = producto_id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.izquierda = None
        self.derecha = None
    
    def __repr__(self):
        return f"Producto(id={self.producto_id}, nombre='{self.nombre}', cantidad={self.cantidad}, precio=${self.precio})"


class ArbolBinarioBusqueda:
    """Implementación de un Árbol Binario de Búsqueda para gestión de productos"""
    
    def __init__(self):
        self.raiz = None
    
    def insertar(self, producto_id, nombre, cantidad, precio):
        """Inserta un nuevo producto en el árbol"""
        if self.raiz is None:
            self.raiz = Nodo(producto_id, nombre, cantidad, precio)
        else:
            self._insertar_recursivo(self.raiz, producto_id, nombre, cantidad, precio)
    
    def _insertar_recursivo(self, nodo, producto_id, nombre, cantidad, precio):
        """Método auxiliar recursivo para insertar"""
        if producto_id < nodo.producto_id:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(producto_id, nombre, cantidad, precio)
            else:
                self._insertar_recursivo(nodo.izquierda, producto_id, nombre, cantidad, precio)
        elif producto_id > nodo.producto_id:
            if nodo.derecha is None:
                nodo.derecha = Nodo(producto_id, nombre, cantidad, precio)
            else:
                self._insertar_recursivo(nodo.derecha, producto_id, nombre, cantidad, precio)
    
    def buscar(self, producto_id):
        """Busca un producto por su ID"""
        return self._buscar_recursivo(self.raiz, producto_id)
    
    def _buscar_recursivo(self, nodo, producto_id):
        """Método auxiliar recursivo para buscar"""
        if nodo is None:
            return None
        
        if producto_id == nodo.producto_id:
            return nodo
        elif producto_id < nodo.producto_id:
            return self._buscar_recursivo(nodo.izquierda, producto_id)
        else:
            return self._buscar_recursivo(nodo.derecha, producto_id)
    
    def eliminar(self, producto_id):
        """Elimina un producto del árbol por su ID"""
        self.raiz = self._eliminar_recursivo(self.raiz, producto_id)
    
    def _eliminar_recursivo(self, nodo, producto_id):
        """Método auxiliar recursivo para eliminar"""
        if nodo is None:
            return None
        
        if producto_id < nodo.producto_id:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, producto_id)
        elif producto_id > nodo.producto_id:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, producto_id)
        else:
            # Nodo a eliminar encontrado
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            else:
                # Nodo con dos hijos
                minimo_nodo = self._encontrar_minimo(nodo.derecha)
                nodo.producto_id = minimo_nodo.producto_id
                nodo.nombre = minimo_nodo.nombre
                nodo.cantidad = minimo_nodo.cantidad
                nodo.precio = minimo_nodo.precio
                nodo.derecha = self._eliminar_recursivo(nodo.derecha, minimo_nodo.producto_id)
        
        return nodo
    
    def _encontrar_minimo(self, nodo):
        """Encuentra el nodo con el ID mínimo en un subárbol"""
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual
    
    def recorrido_inorden(self):
        """Recorrido en orden del árbol (retorna lista ordenada)"""
        resultado = []
        self._recorrido_inorden_recursivo(self.raiz, resultado)
        return resultado
    
    def _recorrido_inorden_recursivo(self, nodo, resultado):
        """Método auxiliar recursivo para recorrido inorden"""
        if nodo is not None:
            self._recorrido_inorden_recursivo(nodo.izquierda, resultado)
            resultado.append(nodo)
            self._recorrido_inorden_recursivo(nodo.derecha, resultado)
    
    def actualizar_cantidad(self, producto_id, nueva_cantidad):
        """Actualiza la cantidad de un producto"""
        nodo = self.buscar(producto_id)
        if nodo:
            nodo.cantidad = nueva_cantidad
            return True
        return False
    
    def obtener_valor_total(self):
        """Calcula el valor total del inventario"""
        def calcular(nodo):
            if nodo is None:
                return 0
            return (nodo.cantidad * nodo.precio) + calcular(nodo.izquierda) + calcular(nodo.derecha)
        
        return calcular(self.raiz)
