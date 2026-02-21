"""
Implementación de Stack (Pila) usando lista de Python.
Estructura de datos LIFO (Last In, First Out).
"""


class Stack:
    """
    Implementación de una Pila (Stack) con operaciones básicas.
    
    Atributos:
        items (list): Lista que almacena los elementos de la pila
    """
    
    def __init__(self):
        """Inicializa una pila vacía."""
        self.items = []
    
    def push(self, item):
        """
        Agrega un elemento al tope de la pila.
        
        Args:
            item: El elemento a agregar
            
        Complejidad: O(1)
        """
        self.items.append(item)
    
    def pop(self):
        """
        Remueve y retorna el elemento del tope de la pila.
        
        Returns:
            El elemento removido del tope de la pila
            
        Raises:
            IndexError: Si la pila está vacía
            
        Complejidad: O(1)
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()
    
    def peek(self):
        """
        Retorna el elemento del tope sin removerlo.
        
        Returns:
            El elemento del tope de la pila
            
        Raises:
            IndexError: Si la pila está vacía
            
        Complejidad: O(1)
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]
    
    def is_empty(self):
        """
        Verifica si la pila está vacía.
        
        Returns:
            bool: True si la pila está vacía, False en caso contrario
            
        Complejidad: O(1)
        """
        return len(self.items) == 0
    
    def size(self):
        """
        Retorna el número de elementos en la pila.
        
        Returns:
            int: Número de elementos en la pila
            
        Complejidad: O(1)
        """
        return len(self.items)
    
    def __str__(self):
        """Representación en string de la pila."""
        return f"Stack({self.items})"
    
    def __repr__(self):
        """Representación oficial de la pila."""
        return f"Stack({self.items})"
