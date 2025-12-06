"""
Visualización del Árbol Binario de Búsqueda
Proporciona una representación visual del estado del árbol
"""

from arbol_binario import ArbolBinarioBusqueda


class VisualizadorBST:
    """Proporciona métodos para visualizar el árbol binario de búsqueda"""
    
    @staticmethod
    def imprimir_arbol(arbol):
        """Imprime el árbol de forma visual"""
        if arbol.raiz is None:
            print("Árbol vacío")
            return
        
        print("\n" + "="*60)
        print("🌳 VISUALIZACIÓN DEL ÁRBOL BINARIO DE BÚSQUEDA")
        print("="*60)
        VisualizadorBST._imprimir_recursivo(arbol.raiz, "", True)
        print("="*60 + "\n")
    
    @staticmethod
    def _imprimir_recursivo(nodo, prefijo, es_ultimo):
        """Imprime recursivamente el árbol con su estructura"""
        if nodo is None:
            return
        
        # Imprimir el nodo actual
        conector = "└── " if es_ultimo else "├── "
        print(prefijo + conector + f"[{nodo.producto_id}] {nodo.nombre} ({nodo.cantidad} units)")
        
        # Preparar prefijo para los hijos
        extension = "    " if es_ultimo else "│   "
        nuevo_prefijo = prefijo + extension
        
        # Determinar si hay hijos
        tiene_izq = nodo.izquierda is not None
        tiene_der = nodo.derecha is not None
        
        # Imprimir hijo izquierdo
        if tiene_izq:
            es_ultimo_izq = not tiene_der
            VisualizadorBST._imprimir_recursivo(nodo.izquierda, nuevo_prefijo, es_ultimo_izq)
        
        # Imprimir hijo derecho
        if tiene_der:
            VisualizadorBST._imprimir_recursivo(nodo.derecha, nuevo_prefijo, True)
    
    @staticmethod
    def imprimir_estadisticas(arbol):
        """Imprime estadísticas del árbol"""
        if arbol.raiz is None:
            print("Árbol vacío - No hay estadísticas")
            return
        
        nodos = arbol.recorrido_inorden()
        altura = VisualizadorBST._calcular_altura(arbol.raiz)
        valor_total = arbol.obtener_valor_total()
        stock_total = sum(n.cantidad for n in nodos)
        
        print("\n" + "="*60)
        print("📊 ESTADÍSTICAS DEL ÁRBOL")
        print("="*60)
        print(f"Cantidad de Nodos: {len(nodos)}")
        print(f"Altura del Árbol: {altura}")
        print(f"Stock Total: {stock_total} unidades")
        print(f"Valor Total del Inventario: ${valor_total:,.2f}")
        
        if len(nodos) > 0:
            precio_promedio = valor_total / len(nodos)
            print(f"Precio Promedio por Producto: ${precio_promedio:,.2f}")
        
        print("="*60 + "\n")
    
    @staticmethod
    def _calcular_altura(nodo):
        """Calcula la altura del árbol recursivamente"""
        if nodo is None:
            return 0
        return 1 + max(VisualizadorBST._calcular_altura(nodo.izquierda),
                       VisualizadorBST._calcular_altura(nodo.derecha))
    
    @staticmethod
    def imprimir_recorridos(arbol):
        """Imprime diferentes recorridos del árbol"""
        if arbol.raiz is None:
            print("Árbol vacío")
            return
        
        print("\n" + "="*60)
        print("📍 RECORRIDOS DEL ÁRBOL")
        print("="*60)
        
        # Recorrido Inorden (izquierda, nodo, derecha)
        inorden = arbol.recorrido_inorden()
        print("Inorden (Izq-Nodo-Der):")
        print(" → ".join([f"[{n.producto_id}]" for n in inorden]))
        
        # Preorden (nodo, izquierda, derecha)
        print("\nPreorden (Nodo-Izq-Der):")
        preorden = []
        VisualizadorBST._preorden(arbol.raiz, preorden)
        print(" → ".join([f"[{n.producto_id}]" for n in preorden]))
        
        # Postorden (izquierda, derecha, nodo)
        print("\nPostorden (Izq-Der-Nodo):")
        postorden = []
        VisualizadorBST._postorden(arbol.raiz, postorden)
        print(" → ".join([f"[{n.producto_id}]" for n in postorden]))
        
        print("="*60 + "\n")
    
    @staticmethod
    def _preorden(nodo, resultado):
        """Recorrido preorden"""
        if nodo is not None:
            resultado.append(nodo)
            VisualizadorBST._preorden(nodo.izquierda, resultado)
            VisualizadorBST._preorden(nodo.derecha, resultado)
    
    @staticmethod
    def _postorden(nodo, resultado):
        """Recorrido postorden"""
        if nodo is not None:
            VisualizadorBST._postorden(nodo.izquierda, resultado)
            VisualizadorBST._postorden(nodo.derecha, resultado)
            resultado.append(nodo)


def ejemplo_visualizacion():
    """Ejemplo de uso del visualizador"""
    print("\n" + "="*70)
    print("🎨 DEMOSTRACIÓN DE VISUALIZACIÓN DEL ÁRBOL BINARIO DE BÚSQUEDA")
    print("="*70)
    
    # Crear árbol y agregar datos
    arbol = ArbolBinarioBusqueda()
    
    productos = [
        (50, "Mouse", 15, 29.99),
        (30, "Teclado", 8, 79.99),
        (70, "Monitor", 3, 299.99),
        (20, "Hub USB", 12, 49.99),
        (40, "Mousepad", 5, 19.99),
        (60, "Webcam", 4, 89.99),
        (80, "Dock", 2, 149.99)
    ]
    
    print("\n📥 Insertando productos en el árbol...")
    for producto_id, nombre, cantidad, precio in productos:
        arbol.insertar(producto_id, nombre, cantidad, precio)
        print(f"  ✓ Insertado: {nombre} (ID: {producto_id})")
    
    # Visualizar el árbol
    VisualizadorBST.imprimir_arbol(arbol)
    
    # Imprimir recorridos
    VisualizadorBST.imprimir_recorridos(arbol)
    
    # Imprimir estadísticas
    VisualizadorBST.imprimir_estadisticas(arbol)
    
    # Simular operaciones
    print("\n🔄 SIMULANDO OPERACIONES:\n")
    
    print("1️⃣  Eliminando nodo hoja (ID: 20)...")
    arbol.eliminar(20)
    VisualizadorBST.imprimir_arbol(arbol)
    
    print("2️⃣  Eliminando nodo con dos hijos (ID: 50)...")
    arbol.eliminar(50)
    VisualizadorBST.imprimir_arbol(arbol)
    
    print("3️⃣  Estado final del árbol:")
    VisualizadorBST.imprimir_estadisticas(arbol)


if __name__ == "__main__":
    ejemplo_visualizacion()
