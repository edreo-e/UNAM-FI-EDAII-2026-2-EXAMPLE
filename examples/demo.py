"""
Programa de demostración de estructuras de datos y algoritmos.

Este archivo muestra ejemplos de uso de todas las estructuras de datos
y algoritmos implementados en el repositorio.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_structures.stack import Stack
from data_structures.queue import Queue
from data_structures.linked_list import LinkedList
from data_structures.binary_tree import BinaryTree
from algorithms.sorting import quick_sort, merge_sort, insertion_sort, bubble_sort
from algorithms.searching import binary_search, linear_search, jump_search
from algorithms.graphs import Graph


def demo_stack():
    """Demostración de Stack (Pila)"""
    print("\n" + "="*50)
    print("DEMOSTRACIÓN: STACK (PILA)")
    print("="*50)
    
    stack = Stack()
    print(f"Stack creado: {stack}")
    
    print("\nAgregando elementos: 10, 20, 30")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(f"Stack: {stack}")
    print(f"Tamaño: {stack.size()}")
    
    print(f"\nPeek (tope): {stack.peek()}")
    print(f"Pop: {stack.pop()}")
    print(f"Stack después de pop: {stack}")


def demo_queue():
    """Demostración de Queue (Cola)"""
    print("\n" + "="*50)
    print("DEMOSTRACIÓN: QUEUE (COLA)")
    print("="*50)
    
    queue = Queue()
    print(f"Queue creada: {queue}")
    
    print("\nAgregando elementos: 10, 20, 30")
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(f"Queue: {queue}")
    print(f"Tamaño: {queue.size()}")
    
    print(f"\nFront (frente): {queue.front()}")
    print(f"Dequeue: {queue.dequeue()}")
    print(f"Queue después de dequeue: {queue}")


def demo_linked_list():
    """Demostración de LinkedList (Lista Enlazada)"""
    print("\n" + "="*50)
    print("DEMOSTRACIÓN: LINKED LIST (LISTA ENLAZADA)")
    print("="*50)
    
    ll = LinkedList()
    print(f"Lista enlazada creada: {ll}")
    
    print("\nAgregando elementos: 10, 20, 30")
    ll.append(10)
    ll.append(20)
    ll.append(30)
    print(f"Lista: {ll}")
    
    print("\nAgregando 5 al inicio")
    ll.prepend(5)
    print(f"Lista: {ll}")
    
    print(f"\n¿Contiene 20?: {ll.search(20)}")
    print(f"¿Contiene 100?: {ll.search(100)}")
    
    print("\nEliminando 20")
    ll.delete(20)
    print(f"Lista: {ll}")


def demo_binary_tree():
    """Demostración de BinaryTree (Árbol Binario)"""
    print("\n" + "="*50)
    print("DEMOSTRACIÓN: BINARY TREE (ÁRBOL BINARIO)")
    print("="*50)
    
    tree = BinaryTree(1)
    tree.insert_left(tree.root, 2)
    tree.insert_right(tree.root, 3)
    tree.insert_left(tree.root.left, 4)
    tree.insert_right(tree.root.left, 5)
    tree.insert_left(tree.root.right, 6)
    tree.insert_right(tree.root.right, 7)
    
    print("Árbol creado con estructura:")
    print("       1")
    print("      / \\")
    print("     2   3")
    print("    / \\ / \\")
    print("   4  5 6  7")
    
    print(f"\nRecorrido Inorden: {tree.inorder_traversal()}")
    print(f"Recorrido Preorden: {tree.preorder_traversal()}")
    print(f"Recorrido Postorden: {tree.postorder_traversal()}")
    print(f"Altura del árbol: {tree.height()}")


def demo_sorting():
    """Demostración de algoritmos de ordenamiento"""
    print("\n" + "="*50)
    print("DEMOSTRACIÓN: ALGORITMOS DE ORDENAMIENTO")
    print("="*50)
    
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"\nArreglo original: {arr}")
    
    print(f"\nQuick Sort: {quick_sort(arr.copy())}")
    print(f"Merge Sort: {merge_sort(arr.copy())}")
    print(f"Insertion Sort: {insertion_sort(arr.copy())}")
    print(f"Bubble Sort: {bubble_sort(arr.copy())}")


def demo_searching():
    """Demostración de algoritmos de búsqueda"""
    print("\n" + "="*50)
    print("DEMOSTRACIÓN: ALGORITMOS DE BÚSQUEDA")
    print("="*50)
    
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 13
    
    print(f"\nArreglo ordenado: {arr}")
    print(f"Buscando: {target}")
    
    index = binary_search(arr, target)
    print(f"\nBinary Search: Encontrado en índice {index}")
    
    index = linear_search(arr, target)
    print(f"Linear Search: Encontrado en índice {index}")
    
    index = jump_search(arr, target)
    print(f"Jump Search: Encontrado en índice {index}")
    
    # Búsqueda de elemento no existente
    target = 100
    print(f"\nBuscando elemento no existente: {target}")
    index = binary_search(arr, target)
    print(f"Binary Search: {index} (no encontrado)")


def demo_graphs():
    """Demostración de algoritmos de grafos"""
    print("\n" + "="*50)
    print("DEMOSTRACIÓN: ALGORITMOS DE GRAFOS")
    print("="*50)
    
    # Crear un grafo no dirigido
    graph = Graph(directed=False)
    
    # Agregar aristas
    edges = [
        (0, 1), (0, 2),
        (1, 2), (1, 3),
        (2, 4),
        (3, 4), (3, 5)
    ]
    
    print("\nConstruyendo grafo con las aristas:")
    for u, v in edges:
        graph.add_edge(u, v)
        print(f"  {u} -- {v}")
    
    start = 0
    print(f"\nRecorrido BFS desde vértice {start}: {graph.bfs(start)}")
    print(f"Recorrido DFS desde vértice {start}: {graph.dfs(start)}")
    print(f"Recorrido DFS iterativo desde vértice {start}: {graph.dfs_iterative(start)}")
    
    print(f"\n¿Existe camino de 0 a 5?: {graph.has_path(0, 5)}")
    print(f"¿Existe camino de 0 a 10?: {graph.has_path(0, 10)}")


def main():
    """Función principal que ejecuta todas las demostraciones"""
    print("\n" + "="*60)
    print(" EJEMPLOS DE ESTRUCTURAS DE DATOS Y ALGORITMOS")
    print(" UNAM - Facultad de Ingeniería")
    print(" EDA-2 / FAC 2026-2")
    print("="*60)
    
    demo_stack()
    demo_queue()
    demo_linked_list()
    demo_binary_tree()
    demo_sorting()
    demo_searching()
    demo_graphs()
    
    print("\n" + "="*60)
    print(" FIN DE DEMOSTRACIONES")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
