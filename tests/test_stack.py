"""
Tests para la implementación de Stack.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_structures.stack import Stack


def test_stack_push_and_pop():
    """Test push y pop operations"""
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1


def test_stack_peek():
    """Test peek operation"""
    stack = Stack()
    stack.push(1)
    stack.push(2)
    
    assert stack.peek() == 2
    assert stack.peek() == 2  # peek no debe remover
    assert stack.size() == 2


def test_stack_is_empty():
    """Test is_empty method"""
    stack = Stack()
    assert stack.is_empty() == True
    
    stack.push(1)
    assert stack.is_empty() == False
    
    stack.pop()
    assert stack.is_empty() == True


def test_stack_size():
    """Test size method"""
    stack = Stack()
    assert stack.size() == 0
    
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.size() == 3
    
    stack.pop()
    assert stack.size() == 2


def test_stack_pop_empty():
    """Test pop from empty stack raises exception"""
    stack = Stack()
    try:
        stack.pop()
        assert False, "Should raise IndexError"
    except IndexError:
        pass


def test_stack_peek_empty():
    """Test peek from empty stack raises exception"""
    stack = Stack()
    try:
        stack.peek()
        assert False, "Should raise IndexError"
    except IndexError:
        pass


if __name__ == "__main__":
    test_stack_push_and_pop()
    test_stack_peek()
    test_stack_is_empty()
    test_stack_size()
    test_stack_pop_empty()
    test_stack_peek_empty()
    print("All stack tests passed!")
