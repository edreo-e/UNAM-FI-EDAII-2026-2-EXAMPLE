# UNAM-FI-EDAII-2026-2-EXAMPLE

Repositorio de ejemplo para la clase de Estructuras de Datos y Algoritmos II (EDA-2) / Fundamentos de Ciencias de la Computación (FAC) - Facultad de Ingeniería, UNAM.

## Descripción

Este repositorio contiene implementaciones de referencia de estructuras de datos y algoritmos fundamentales en Python, diseñado como material educativo para estudiantes de ingeniería.

## Contenido

### Estructuras de Datos
- **Stack (Pila)**: Implementación de pila con operaciones LIFO
- **Queue (Cola)**: Implementación de cola con operaciones FIFO
- **Linked List (Lista Enlazada)**: Lista enlazada simple con operaciones básicas
- **Binary Tree (Árbol Binario)**: Árbol binario con recorridos (inorden, preorden, postorden)

### Algoritmos
- **Algoritmos de Ordenamiento**:
  - Quick Sort
  - Merge Sort
  - Insertion Sort
- **Algoritmos de Búsqueda**:
  - Búsqueda Binaria
  - Búsqueda Lineal
- **Algoritmos de Grafos**:
  - BFS (Breadth-First Search)
  - DFS (Depth-First Search)

## Estructura del Proyecto

```
.
├── data_structures/          # Implementaciones de estructuras de datos
│   ├── stack.py
│   ├── queue.py
│   ├── linked_list.py
│   └── binary_tree.py
├── algorithms/               # Implementaciones de algoritmos
│   ├── sorting.py
│   ├── searching.py
│   └── graphs.py
├── tests/                    # Tests unitarios
│   ├── test_stack.py
│   ├── test_queue.py
│   ├── test_linked_list.py
│   └── test_binary_tree.py
├── examples/                 # Ejemplos de uso
│   └── demo.py
└── README.md
```

## Requisitos

- Python 3.7 o superior

## Instalación

1. Clone el repositorio:
```bash
git clone https://github.com/edreo-e/UNAM-FI-EDAII-2026-2-EXAMPLE.git
cd UNAM-FI-EDAII-2026-2-EXAMPLE
```

2. (Opcional) Cree un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

## Uso

### Ejemplo de Stack (Pila)
```python
from data_structures.stack import Stack

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # 3
```

### Ejemplo de Queue (Cola)
```python
from data_structures.queue import Queue

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())  # 1
```

### Ejemplo de Búsqueda Binaria
```python
from algorithms.searching import binary_search

arr = [1, 3, 5, 7, 9, 11, 13]
index = binary_search(arr, 7)
print(f"Elemento encontrado en índice: {index}")
```

## Ejecución de Tests

```bash
python -m pytest tests/
```

## Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Haga un fork del repositorio
2. Cree una rama para su feature (`git checkout -b feature/nueva-caracteristica`)
3. Commit sus cambios (`git commit -m 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abra un Pull Request

## Licencia

Este proyecto es material educativo de código abierto para uso académico.

## Autores

Facultad de Ingeniería - UNAM
Curso: Estructuras de Datos y Algoritmos II (2026-2)