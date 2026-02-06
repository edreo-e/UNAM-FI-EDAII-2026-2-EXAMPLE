"""
Implementaciones de algoritmos de ordenamiento.
"""


def quick_sort(arr):
    """
    Algoritmo Quick Sort (ordenamiento rápido).
    
    Utiliza el paradigma divide y vencerás, seleccionando un pivote
    y particionando el arreglo en elementos menores y mayores al pivote.
    
    Args:
        arr (list): Lista a ordenar
        
    Returns:
        list: Lista ordenada
        
    Complejidad:
        - Mejor caso: O(n log n)
        - Caso promedio: O(n log n)
        - Peor caso: O(n²)
    Espacio: O(log n) por la recursión
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr):
    """
    Algoritmo Merge Sort (ordenamiento por mezcla).
    
    Divide recursivamente el arreglo en mitades hasta tener elementos
    individuales, luego los combina de manera ordenada.
    
    Args:
        arr (list): Lista a ordenar
        
    Returns:
        list: Lista ordenada
        
    Complejidad: O(n log n) en todos los casos
    Espacio: O(n)
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left, right):
    """
    Función auxiliar para merge_sort que combina dos listas ordenadas.
    
    Args:
        left (list): Lista ordenada izquierda
        right (list): Lista ordenada derecha
        
    Returns:
        list: Lista combinada y ordenada
    """
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


def insertion_sort(arr):
    """
    Algoritmo Insertion Sort (ordenamiento por inserción).
    
    Construye el arreglo ordenado un elemento a la vez, insertando
    cada elemento en su posición correcta.
    
    Args:
        arr (list): Lista a ordenar
        
    Returns:
        list: Lista ordenada
        
    Complejidad:
        - Mejor caso: O(n) cuando ya está ordenado
        - Caso promedio: O(n²)
        - Peor caso: O(n²)
    Espacio: O(1) - ordenamiento in-place
    """
    sorted_arr = arr.copy()
    
    for i in range(1, len(sorted_arr)):
        key = sorted_arr[i]
        j = i - 1
        
        while j >= 0 and sorted_arr[j] > key:
            sorted_arr[j + 1] = sorted_arr[j]
            j -= 1
        
        sorted_arr[j + 1] = key
    
    return sorted_arr


def bubble_sort(arr):
    """
    Algoritmo Bubble Sort (ordenamiento de burbuja).
    
    Compara repetidamente elementos adyacentes e intercambia
    los que están en el orden incorrecto.
    
    Args:
        arr (list): Lista a ordenar
        
    Returns:
        list: Lista ordenada
        
    Complejidad:
        - Mejor caso: O(n) con optimización
        - Caso promedio: O(n²)
        - Peor caso: O(n²)
    Espacio: O(1)
    """
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return sorted_arr
