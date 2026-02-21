"""
Implementación de Queue (Cola) usando lista de Python.
Estructura de datos FIFO (First In, First Out).
"""


class Queue:
    """
    Implementación de una Cola (Queue) con operaciones básicas.
    
    Atributos:
        items (list): Lista que almacena los elementos de la cola
    """
    
    def __init__(self):
        """Inicializa una cola vacía."""
        self.items = []
    
    def enqueue(self, item):
        """
        Agrega un elemento al final de la cola.
        
        Args:
            item: El elemento a agregar
            
        Complejidad: O(1) amortizado
        """
        self.items.append(item)
    
    def dequeue(self):
        """
        Remueve y retorna el elemento del frente de la cola.
        
        Returns:
            El elemento removido del frente de la cola
            
        Raises:
            IndexError: Si la cola está vacía
            
        Complejidad: O(n) debido al desplazamiento de elementos
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)
    
    def front(self):
        """
        Retorna el elemento del frente sin removerlo.
        
        Returns:
            El elemento del frente de la cola
            
        Raises:
            IndexError: Si la cola está vacía
            
        Complejidad: O(1)
        """
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self.items[0]
    
    def is_empty(self):
        """
        Verifica si la cola está vacía.
        
        Returns:
            bool: True si la cola está vacía, False en caso contrario
            
        Complejidad: O(1)
        """
        return len(self.items) == 0
    
    def size(self):
        """
        Retorna el número de elementos en la cola.
        
        Returns:
            int: Número de elementos en la cola
            
        Complejidad: O(1)
        """
        return len(self.items)
    
    def __str__(self):
        """Representación en string de la cola."""
        return f"Queue({self.items})"
    
    def __repr__(self):
        """Representación oficial de la cola."""
        return f"Queue({self.items})"
