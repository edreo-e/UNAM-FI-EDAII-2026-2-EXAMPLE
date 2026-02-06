"""
Implementación de Árbol Binario (Binary Tree).
Estructura de datos jerárquica con nodos con máximo dos hijos.
"""


class TreeNode:
    """
    Nodo de un árbol binario.
    
    Atributos:
        data: Datos almacenados en el nodo
        left: Referencia al hijo izquierdo
        right: Referencia al hijo derecho
    """
    
    def __init__(self, data):
        """
        Inicializa un nodo del árbol.
        
        Args:
            data: Los datos a almacenar en el nodo
        """
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    """
    Implementación de un Árbol Binario con recorridos básicos.
    
    Atributos:
        root: Referencia al nodo raíz del árbol
    """
    
    def __init__(self, root_data=None):
        """
        Inicializa un árbol binario.
        
        Args:
            root_data: Datos opcionales para el nodo raíz
        """
        self.root = TreeNode(root_data) if root_data is not None else None
    
    def insert_left(self, node, data):
        """
        Inserta un nodo como hijo izquierdo.
        
        Args:
            node: El nodo padre
            data: Los datos del nuevo nodo
            
        Returns:
            TreeNode: El nodo insertado
        """
        if node is None:
            return None
        
        new_node = TreeNode(data)
        node.left = new_node
        return new_node
    
    def insert_right(self, node, data):
        """
        Inserta un nodo como hijo derecho.
        
        Args:
            node: El nodo padre
            data: Los datos del nuevo nodo
            
        Returns:
            TreeNode: El nodo insertado
        """
        if node is None:
            return None
        
        new_node = TreeNode(data)
        node.right = new_node
        return new_node
    
    def inorder_traversal(self, node=None, _is_first_call=True):
        """
        Recorrido inorden (izquierda-raíz-derecha) del árbol.
        
        Args:
            node: Nodo desde donde comenzar (por defecto la raíz)
            
        Returns:
            list: Lista con los elementos en orden inorden
            
        Complejidad: O(n)
        """
        if node is None and _is_first_call:
            node = self.root
        
        result = []
        if node:
            result.extend(self.inorder_traversal(node.left, _is_first_call=False))
            result.append(node.data)
            result.extend(self.inorder_traversal(node.right, _is_first_call=False))
        
        return result
    
    def preorder_traversal(self, node=None, _is_first_call=True):
        """
        Recorrido preorden (raíz-izquierda-derecha) del árbol.
        
        Args:
            node: Nodo desde donde comenzar (por defecto la raíz)
            
        Returns:
            list: Lista con los elementos en orden preorden
            
        Complejidad: O(n)
        """
        if node is None and _is_first_call:
            node = self.root
        
        result = []
        if node:
            result.append(node.data)
            result.extend(self.preorder_traversal(node.left, _is_first_call=False))
            result.extend(self.preorder_traversal(node.right, _is_first_call=False))
        
        return result
    
    def postorder_traversal(self, node=None, _is_first_call=True):
        """
        Recorrido postorden (izquierda-derecha-raíz) del árbol.
        
        Args:
            node: Nodo desde donde comenzar (por defecto la raíz)
            
        Returns:
            list: Lista con los elementos en orden postorden
            
        Complejidad: O(n)
        """
        if node is None and _is_first_call:
            node = self.root
        
        result = []
        if node:
            result.extend(self.postorder_traversal(node.left, _is_first_call=False))
            result.extend(self.postorder_traversal(node.right, _is_first_call=False))
            result.append(node.data)
        
        return result
    
    def height(self, node=None, _is_first_call=True):
        """
        Calcula la altura del árbol.
        
        Args:
            node: Nodo desde donde calcular (por defecto la raíz)
            
        Returns:
            int: Altura del árbol
            
        Complejidad: O(n)
        """
        if node is None and _is_first_call:
            node = self.root
        
        if node is None:
            return 0
        
        left_height = self.height(node.left, _is_first_call=False)
        right_height = self.height(node.right, _is_first_call=False)
        
        return max(left_height, right_height) + 1
    
    def is_empty(self):
        """
        Verifica si el árbol está vacío.
        
        Returns:
            bool: True si el árbol está vacío, False en caso contrario
        """
        return self.root is None
    
    def __str__(self):
        """Representación en string del árbol."""
        if self.is_empty():
            return "BinaryTree(empty)"
        return f"BinaryTree(inorder: {self.inorder_traversal()})"
    
    def __repr__(self):
        """Representación oficial del árbol."""
        return self.__str__()
