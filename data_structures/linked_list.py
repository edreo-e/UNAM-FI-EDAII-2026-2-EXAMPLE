"""
Implementación de Lista Enlazada (Linked List).
Estructura de datos lineal con nodos enlazados.
"""


class Node:
    """
    Nodo individual de una lista enlazada.
    
    Atributos:
        data: Datos almacenados en el nodo
        next: Referencia al siguiente nodo
    """
    
    def __init__(self, data):
        """
        Inicializa un nodo con datos.
        
        Args:
            data: Los datos a almacenar en el nodo
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    Implementación de una Lista Enlazada Simple.
    
    Atributos:
        head: Referencia al primer nodo de la lista
    """
    
    def __init__(self):
        """Inicializa una lista enlazada vacía."""
        self.head = None
    
    def append(self, data):
        """
        Agrega un elemento al final de la lista.
        
        Args:
            data: El elemento a agregar
            
        Complejidad: O(n)
        """
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def prepend(self, data):
        """
        Agrega un elemento al inicio de la lista.
        
        Args:
            data: El elemento a agregar
            
        Complejidad: O(1)
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, data):
        """
        Elimina la primera ocurrencia de un elemento.
        
        Args:
            data: El elemento a eliminar
            
        Returns:
            bool: True si se eliminó, False si no se encontró
            
        Complejidad: O(n)
        """
        if self.head is None:
            return False
        
        if self.head.data == data:
            self.head = self.head.next
            return True
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return True
            current = current.next
        
        return False
    
    def search(self, data):
        """
        Busca un elemento en la lista.
        
        Args:
            data: El elemento a buscar
            
        Returns:
            bool: True si se encuentra, False en caso contrario
            
        Complejidad: O(n)
        """
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def is_empty(self):
        """
        Verifica si la lista está vacía.
        
        Returns:
            bool: True si la lista está vacía, False en caso contrario
            
        Complejidad: O(1)
        """
        return self.head is None
    
    def size(self):
        """
        Retorna el número de elementos en la lista.
        
        Returns:
            int: Número de elementos
            
        Complejidad: O(n)
        """
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def to_list(self):
        """
        Convierte la lista enlazada a una lista de Python.
        
        Returns:
            list: Lista con los elementos
            
        Complejidad: O(n)
        """
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def __str__(self):
        """Representación en string de la lista enlazada."""
        return f"LinkedList({self.to_list()})"
    
    def __repr__(self):
        """Representación oficial de la lista enlazada."""
        return f"LinkedList({self.to_list()})"
