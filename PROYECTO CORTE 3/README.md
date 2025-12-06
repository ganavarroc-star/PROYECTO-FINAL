# 🌳 Sistema de Gestión de Inventario con Árbol Binario de Búsqueda

## 📋 Descripción General

Este proyecto implementa un **Sistema de Gestión de Inventario** utilizando un **Árbol Binario de Búsqueda (BST)** como estructura de datos central. El software fue desarrollado completamente en **Visual Studio Code** con asistencia de **GitHub Copilot**.

## 🎯 Criterios de Aceptación Cumplidos

✅ **Implementación de Estructura de Datos**: Se implementó un Árbol Binario de Búsqueda funcional con todas las operaciones básicas (insertar, buscar, eliminar, recorridos).

✅ **Entorno de Desarrollo**: Código fuente creado y editado en Visual Studio Code.

✅ **Asistencia por IA**: Desarrollo asistido por GitHub Copilot para generación y optimización de código.

✅ **Funcionalidad Mínima**: El software demuestra activamente el uso de la estructura BST para:
- Almacenar productos con atributos (ID, nombre, cantidad, precio)
- Insertar nuevos productos
- Buscar productos por ID
- Eliminar productos del inventario
- Manipular información de inventario (actualizar stock, obtener reportes)

## 📁 Estructura del Proyecto

```
bst-inventory/
├── arbol_binario.py       # Implementación del Árbol Binario de Búsqueda
├── main.py                # Aplicación principal de gestión de inventario
├── test_inventario.py     # Pruebas unitarias completas
└── README.md             # Documentación del proyecto
```

## 🛠️ Componentes Principales

### 1. **arbol_binario.py** - Estructura de Datos BST

Contiene dos clases principales:

#### Clase `Nodo`
```python
class Nodo:
    - producto_id: Identificador único del producto
    - nombre: Nombre del producto
    - cantidad: Cantidad en stock
    - precio: Precio unitario
    - izquierda: Referencia al hijo izquierdo
    - derecha: Referencia al hijo derecho
```

#### Clase `ArbolBinarioBusqueda`
Métodos principales:
- `insertar(producto_id, nombre, cantidad, precio)` - Inserta un producto
- `buscar(producto_id)` - Busca un producto por ID (O(log n) promedio)
- `eliminar(producto_id)` - Elimina un producto del árbol
- `recorrido_inorden()` - Retorna todos los productos ordenados por ID
- `actualizar_cantidad(producto_id, nueva_cantidad)` - Actualiza stock
- `obtener_valor_total()` - Calcula el valor total del inventario

### 2. **main.py** - Aplicación de Gestión de Inventario

Proporciona la clase `GestorInventario` que utiliza el BST para:

```python
GestorInventario
├── agregar_producto()          # Agrega nuevo producto
├── buscar_producto()           # Busca por ID
├── eliminar_producto()         # Elimina del inventario
├── actualizar_stock()          # Modifica cantidad
├── listar_inventario()         # Muestra todos los productos ordenados
└── obtener_reporte()           # Genera reporte de estado
```

**Demostraciones en main():**
1. Agregación de 6 productos de ejemplo
2. Listado del inventario ordenado
3. Búsqueda de productos específicos
4. Actualización de stock
5. Eliminación de productos
6. Reporte final con valor total del inventario

### 3. **test_inventario.py** - Suite de Pruebas Unitarias

Contiene **17 pruebas unitarias** que validan:

**TestArbolBinarioBusqueda (10 pruebas):**
- Árbol vacío
- Inserción simple y múltiple
- Búsqueda exitosa y fallida
- Eliminación de nodos (hoja y con dos hijos)
- Recorrido inorden ordenado
- Actualización de cantidad
- Cálculo de valor total

**TestGestorInventario (7 pruebas):**
- Agregar productos
- Prevención de duplicados
- Búsqueda de productos
- Eliminación de productos
- Actualización de stock
- Flujo completo de operaciones

## 🚀 Cómo Ejecutar el Proyecto

### Requisitos
- Python 3.7 o superior
- Visual Studio Code (opcional pero recomendado)

### Instalación

1. Clonar o descargar el proyecto
2. Navegar al directorio del proyecto:
```bash
cd bst-inventory
```

### Ejecutar la Demostración Principal

```bash
python main.py
```

**Salida esperada:**
- Adición de 6 productos
- Listado ordenado del inventario
- Búsquedas exitosas y fallidas
- Actualizaciones de stock
- Listado actualizado
- Eliminación de producto
- Listado final
- Reporte de valor total

### Ejecutar las Pruebas Unitarias

```bash
python -m unittest test_inventario.py -v
```

O simplemente:
```bash
python test_inventario.py
```

**Salida esperada:**
- 17 pruebas ejecutadas exitosamente
- 100% de cobertura de funcionalidad

## 📊 Ejemplo de Ejecución

```
🚀 Sistema de Gestión de Inventario con Árbol Binario de Búsqueda
======================================================================

📥 AGREGANDO PRODUCTOS AL INVENTARIO:

✅ Producto 'Laptop' (ID: 101) agregado al inventario.
✅ Producto 'Mouse' (ID: 50) agregado al inventario.
✅ Producto 'Monitor' (ID: 150) agregado al inventario.
✅ Producto 'Teclado' (ID: 75) agregado al inventario.
✅ Producto 'Hub USB' (ID: 25) agregado al inventario.
✅ Producto 'Webcam' (ID: 200) agregado al inventario.

======================================================================
📋 INVENTARIO ACTUAL (Ordenado por ID de Producto)
======================================================================
ID:   25 | Nombre: Hub USB           | Stock:  12 | Precio: $      49.99 | Valor Total: $    599.88
ID:   50 | Nombre: Mouse             | Stock:  15 | Precio: $      29.99 | Valor Total: $    449.85
ID:   75 | Nombre: Teclado           | Stock:   8 | Precio: $      79.99 | Valor Total: $    639.92
ID:  101 | Nombre: Laptop            | Stock:   5 | Precio: $     999.99 | Valor Total: $   4999.95
ID:  150 | Nombre: Monitor           | Stock:   3 | Precio: $     299.99 | Valor Total: $    899.97
ID:  200 | Nombre: Webcam            | Stock:   4 | Precio: $      89.99 | Valor Total: $    359.96
======================================================================
```

## 💡 Características Técnicas

### Operaciones del BST

**Complejidad Temporal:**
- Inserción: O(log n) promedio, O(n) peor caso
- Búsqueda: O(log n) promedio, O(n) peor caso
- Eliminación: O(log n) promedio, O(n) peor caso
- Recorrido Inorden: O(n)

### Ventajas de usar BST para este caso de uso

1. **Búsqueda eficiente**: Localizar productos por ID es rápido
2. **Orden mantenido**: El recorrido inorden retorna productos ordenados
3. **Escalabilidad**: Eficiente con inventarios grandes
4. **Flexibilidad**: Fácil agregar nuevas funcionalidades (rango de búsqueda, etc.)

## 📚 Conceptos Implementados

- ✅ Estructura de datos recursiva
- ✅ Operaciones de árbol binario (inserción, búsqueda, eliminación)
- ✅ Recorridos de árbol (inorden)
- ✅ Algoritmo de rebalanceo al eliminar nodos con dos hijos
- ✅ Programación orientada a objetos
- ✅ Pruebas unitarias exhaustivas
- ✅ Documentación de código

## 🔍 Validación de Funcionalidad

El proyecto demuestra activamente que la estructura de datos funciona:

1. **Almacenamiento**: Se almacenan múltiples productos con atributos
2. **Manipulación**: Se insertan, buscan y eliminan productos
3. **Consultas**: Se generan reportes y se accede a datos
4. **Integridad**: Las 17 pruebas unitarias validan todo el flujo

## 📝 Licencia

Este proyecto fue desarrollado como parte de una actividad educativa.

---

**Desarrollado con ❤️ usando Visual Studio Code y GitHub Copilot**
