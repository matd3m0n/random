from ipdb import set_trace
from typing import List

        
class Node:
    '''
    The Node class represents a node in a binary tree.

    Each node has a value associated with it and may have left and right child nodes.

    Methods:
        __init__(value): Initializes a new instance of the Node class.
        __str__(): Returns a string representation of the node.
        get_children(): Retrieves the non-null children of the node.
        is_leaf(): Checks if the node is a leaf node.
    '''
    def __init__(self, value: int) -> None:
        '''
        Initializes a new instance of the Node class.

        Args:
            value: The value associated with the node.
        '''
        self.value = value
        self.left = None
        self.right = None

    def __str__(self) -> str:
        '''
        Returns a string representation of the node.

        The string format is 'value: (left_value, right_value)'.

        Returns:
            A string representation of the node.
        '''
        tl = 0 if self.left is None else self.left.value
        tr = 0 if self.right is None else self.right.value
        return '%d: (%d, %d)'%(self.value, tl, tr)

    def get_children(self) -> List['Node']:
        '''
        Retrieves the non-null children of the node.

        Returns:
            A list of non-null children nodes.
        '''
        children = [child for child in [self.left, self.right]\
                if child is not None]
        return children

    def is_leaf(self) -> bool:
        '''
        Checks if the node is a leaf node.

        Returns:
            True if the node is a leaf node, False otherwise.
        '''
        return True if self.left is None and self.right is None else False


