"""
Tests para la implementación de Queue.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_structures.queue import Queue


def test_queue_enqueue_and_dequeue():
    """Test enqueue y dequeue operations"""
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3


def test_queue_front():
    """Test front operation"""
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    
    assert queue.front() == 1
    assert queue.front() == 1  # front no debe remover
    assert queue.size() == 2


def test_queue_is_empty():
    """Test is_empty method"""
    queue = Queue()
    assert queue.is_empty() == True
    
    queue.enqueue(1)
    assert queue.is_empty() == False
    
    queue.dequeue()
    assert queue.is_empty() == True


def test_queue_size():
    """Test size method"""
    queue = Queue()
    assert queue.size() == 0
    
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.size() == 3
    
    queue.dequeue()
    assert queue.size() == 2


def test_queue_dequeue_empty():
    """Test dequeue from empty queue raises exception"""
    queue = Queue()
    try:
        queue.dequeue()
        assert False, "Should raise IndexError"
    except IndexError:
        pass


def test_queue_front_empty():
    """Test front from empty queue raises exception"""
    queue = Queue()
    try:
        queue.front()
        assert False, "Should raise IndexError"
    except IndexError:
        pass


if __name__ == "__main__":
    test_queue_enqueue_and_dequeue()
    test_queue_front()
    test_queue_is_empty()
    test_queue_size()
    test_queue_dequeue_empty()
    test_queue_front_empty()
    print("All queue tests passed!")
