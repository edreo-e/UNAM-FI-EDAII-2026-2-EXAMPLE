"""
Tests para la implementación de LinkedList.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_structures.linked_list import LinkedList


def test_linked_list_append():
    """Test append operation"""
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    
    assert ll.to_list() == [1, 2, 3]


def test_linked_list_prepend():
    """Test prepend operation"""
    ll = LinkedList()
    ll.prepend(1)
    ll.prepend(2)
    ll.prepend(3)
    
    assert ll.to_list() == [3, 2, 1]


def test_linked_list_delete():
    """Test delete operation"""
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    
    assert ll.delete(2) == True
    assert ll.to_list() == [1, 3]
    
    assert ll.delete(5) == False
    assert ll.to_list() == [1, 3]


def test_linked_list_search():
    """Test search operation"""
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    
    assert ll.search(2) == True
    assert ll.search(5) == False


def test_linked_list_is_empty():
    """Test is_empty method"""
    ll = LinkedList()
    assert ll.is_empty() == True
    
    ll.append(1)
    assert ll.is_empty() == False


def test_linked_list_size():
    """Test size method"""
    ll = LinkedList()
    assert ll.size() == 0
    
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.size() == 3


if __name__ == "__main__":
    test_linked_list_append()
    test_linked_list_prepend()
    test_linked_list_delete()
    test_linked_list_search()
    test_linked_list_is_empty()
    test_linked_list_size()
    print("All linked list tests passed!")
