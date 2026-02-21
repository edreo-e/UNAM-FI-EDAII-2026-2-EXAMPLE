"""
Implementaciones de algoritmos de grafos.
"""

from collections import deque, defaultdict


class Graph:
    """
    Representación de un grafo usando lista de adyacencia.
    
    Atributos:
        graph (dict): Diccionario que mapea vértices a sus adyacentes
        directed (bool): Indica si el grafo es dirigido o no
    """
    
    def __init__(self, directed=False):
        """
        Inicializa un grafo vacío.
        
        Args:
            directed (bool): True para grafo dirigido, False para no dirigido
        """
        self.graph = defaultdict(list)
        self.directed = directed
    
    def add_edge(self, u, v):
        """
        Agrega una arista al grafo.
        
        Args:
            u: Vértice origen
            v: Vértice destino
        """
        self.graph[u].append(v)
        
        if not self.directed:
            self.graph[v].append(u)
    
    def bfs(self, start):
        """
        Recorrido BFS (Breadth-First Search / Búsqueda en Anchura).
        
        Explora el grafo por niveles, visitando todos los vecinos
        de un vértice antes de pasar a sus vecinos.
        
        Args:
            start: Vértice inicial
            
        Returns:
            list: Lista de vértices en orden de visita BFS
            
        Complejidad: O(V + E) donde V=vértices, E=aristas
        Espacio: O(V)
        """
        visited = set()
        queue = deque([start])
        visited.add(start)
        result = []
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    def dfs(self, start):
        """
        Recorrido DFS (Depth-First Search / Búsqueda en Profundidad).
        
        Explora el grafo tan profundo como sea posible antes de retroceder.
        
        Args:
            start: Vértice inicial
            
        Returns:
            list: Lista de vértices en orden de visita DFS
            
        Complejidad: O(V + E) donde V=vértices, E=aristas
        Espacio: O(V)
        """
        visited = set()
        result = []
        
        self._dfs_recursive(start, visited, result)
        
        return result
    
    def _dfs_recursive(self, vertex, visited, result):
        """
        Función auxiliar recursiva para DFS.
        
        Args:
            vertex: Vértice actual
            visited (set): Conjunto de vértices visitados
            result (list): Lista de resultados
        """
        visited.add(vertex)
        result.append(vertex)
        
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited, result)
    
    def dfs_iterative(self, start):
        """
        Implementación iterativa de DFS usando una pila.
        
        Args:
            start: Vértice inicial
            
        Returns:
            list: Lista de vértices en orden de visita DFS
            
        Complejidad: O(V + E)
        Espacio: O(V)
        """
        visited = set()
        stack = [start]
        result = []
        
        while stack:
            vertex = stack.pop()
            
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                
                # Agregar vecinos en orden inverso para mantener orden correcto
                for neighbor in reversed(self.graph[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return result
    
    def has_path(self, start, end):
        """
        Verifica si existe un camino entre dos vértices usando BFS.
        
        Args:
            start: Vértice inicial
            end: Vértice final
            
        Returns:
            bool: True si existe un camino, False en caso contrario
            
        Complejidad: O(V + E)
        """
        if start == end:
            return True
        
        visited = set()
        queue = deque([start])
        visited.add(start)
        
        while queue:
            vertex = queue.popleft()
            
            if vertex == end:
                return True
            
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return False
    
    def get_vertices(self):
        """
        Retorna todos los vértices del grafo.
        
        Returns:
            list: Lista de vértices
        """
        vertices = set(self.graph.keys())
        for neighbors in self.graph.values():
            vertices.update(neighbors)
        return list(vertices)
    
    def __str__(self):
        """Representación en string del grafo."""
        return f"Graph({dict(self.graph)})"
    
    def __repr__(self):
        """Representación oficial del grafo."""
        return self.__str__()
