"""
Implementaciones de algoritmos de búsqueda.
"""


def binary_search(arr, target):
    """
    Algoritmo de Búsqueda Binaria.
    
    Busca un elemento en un arreglo ordenado dividiendo repetidamente
    el espacio de búsqueda a la mitad.
    
    Args:
        arr (list): Lista ordenada donde buscar
        target: Elemento a buscar
        
    Returns:
        int: Índice del elemento si se encuentra, -1 si no existe
        
    Complejidad: O(log n)
    Espacio: O(1)
    
    Nota: El arreglo debe estar ordenado.
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def binary_search_recursive(arr, target, left=0, right=None):
    """
    Implementación recursiva de Búsqueda Binaria.
    
    Args:
        arr (list): Lista ordenada donde buscar
        target: Elemento a buscar
        left (int): Índice izquierdo del rango de búsqueda
        right (int): Índice derecho del rango de búsqueda
        
    Returns:
        int: Índice del elemento si se encuentra, -1 si no existe
        
    Complejidad: O(log n)
    Espacio: O(log n) por la recursión
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def linear_search(arr, target):
    """
    Algoritmo de Búsqueda Lineal.
    
    Busca un elemento recorriendo secuencialmente el arreglo.
    
    Args:
        arr (list): Lista donde buscar
        target: Elemento a buscar
        
    Returns:
        int: Índice del elemento si se encuentra, -1 si no existe
        
    Complejidad: O(n)
    Espacio: O(1)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def jump_search(arr, target):
    """
    Algoritmo de Búsqueda por Saltos.
    
    Salta bloques del arreglo para encontrar el rango donde puede
    estar el elemento, luego hace búsqueda lineal en ese rango.
    
    Args:
        arr (list): Lista ordenada donde buscar
        target: Elemento a buscar
        
    Returns:
        int: Índice del elemento si se encuentra, -1 si no existe
        
    Complejidad: O(√n)
    Espacio: O(1)
    
    Nota: El arreglo debe estar ordenado.
    """
    import math
    
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    
    # Encontrar el bloque donde podría estar el elemento
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        
        if prev >= n:
            return -1
    
    # Búsqueda lineal en el bloque
    while arr[prev] < target:
        prev += 1
        
        if prev == min(step, n):
            return -1
    
    # Si encontramos el elemento
    if arr[prev] == target:
        return prev
    
    return -1
