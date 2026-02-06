"""
Tests para la implementación de BinaryTree.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_structures.binary_tree import BinaryTree


def test_binary_tree_creation():
    """Test tree creation"""
    tree = BinaryTree(1)
    assert tree.root.data == 1


def test_binary_tree_insert():
    """Test insert operations"""
    tree = BinaryTree(1)
    left_node = tree.insert_left(tree.root, 2)
    right_node = tree.insert_right(tree.root, 3)
    
    assert tree.root.left.data == 2
    assert tree.root.right.data == 3


def test_binary_tree_inorder():
    """Test inorder traversal"""
    tree = BinaryTree(1)
    tree.insert_left(tree.root, 2)
    tree.insert_right(tree.root, 3)
    tree.insert_left(tree.root.left, 4)
    tree.insert_right(tree.root.left, 5)
    
    assert tree.inorder_traversal() == [4, 2, 5, 1, 3]


def test_binary_tree_preorder():
    """Test preorder traversal"""
    tree = BinaryTree(1)
    tree.insert_left(tree.root, 2)
    tree.insert_right(tree.root, 3)
    tree.insert_left(tree.root.left, 4)
    tree.insert_right(tree.root.left, 5)
    
    assert tree.preorder_traversal() == [1, 2, 4, 5, 3]


def test_binary_tree_postorder():
    """Test postorder traversal"""
    tree = BinaryTree(1)
    tree.insert_left(tree.root, 2)
    tree.insert_right(tree.root, 3)
    tree.insert_left(tree.root.left, 4)
    tree.insert_right(tree.root.left, 5)
    
    assert tree.postorder_traversal() == [4, 5, 2, 3, 1]


def test_binary_tree_height():
    """Test height calculation"""
    tree = BinaryTree(1)
    assert tree.height() == 1
    
    tree.insert_left(tree.root, 2)
    tree.insert_right(tree.root, 3)
    assert tree.height() == 2
    
    tree.insert_left(tree.root.left, 4)
    assert tree.height() == 3


def test_binary_tree_is_empty():
    """Test is_empty method"""
    tree = BinaryTree()
    assert tree.is_empty() == True
    
    tree = BinaryTree(1)
    assert tree.is_empty() == False


if __name__ == "__main__":
    test_binary_tree_creation()
    test_binary_tree_insert()
    test_binary_tree_inorder()
    test_binary_tree_preorder()
    test_binary_tree_postorder()
    test_binary_tree_height()
    test_binary_tree_is_empty()
    print("All binary tree tests passed!")
