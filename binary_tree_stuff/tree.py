from ipdb import set_trace
from iterators import BFS_iter


class NodeInsertionError(Exception):
    '''
    Custom exception raised when a node cannot be inserted into a tree.

    Inherits:
        Exception: The base class for all exceptions.

    Example Usage:
        raise NodeInsertionError("Cannot insert node")
    '''
    def __init__(self, message):
        '''
        Initializes a new instance of the NodeInsertionError class.

        Args:
            message: The error message associated with the exception.
        '''
        super().__init__(message)

class Tree:
    '''
    The Tree class represents a binary tree data structure.

    Methods:
        __init__(root): Initializes a new instance of the Tree class.
        insert_node(nn): Inserts a new node into the tree using breadth-first search.

    Attributes:
        root: The root node of the binary tree.

    Example Usage:
        tree = Tree(root_node)
        new_node = Node(value)
        tree.insert_node(new_node)

    '''
    def __init__(self, root):
        '''
        Initializes a new instance of the Tree class.

        Args:
            root: The root node of the binary tree.
        '''
        self.root = root

    def insert_node(self, nn):
        '''
        Inserts a new node into the tree using breadth-first search.

        The method traverses the tree using breadth-first search and finds 
        the first available position to insert the new node.
        If a node has an empty left child, the new node is inserted as the 
        left child.
        If a node has an empty right child, the new node is inserted as the 
        right child.

        Args:
            nn: The node to be inserted.

        Returns:
            True if the node is successfully inserted, err otherwise.

        Example Usage:
            tree = Tree(root_node)
            new_node = Node(value)
            tree.insert_node(new_node)
        '''
        for node in BFS_iter(self):
            if node.left is None:
                node.left = nn
                return True
            elif node.right is None:
                node.right = nn
                return True
        raise NodeInsertionError("Node not inserted")


