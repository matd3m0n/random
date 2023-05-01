from ipdb import set_trace
import re
from typing import List, Union

from binary_tree.iterators import BFS_iter
from binary_tree.node import Node


class Tree:
    '''
    The Tree class represents a binary tree data structure.

    Methods:
        __init__(root): Initializes a new instance of the Tree class.
        from_encoding_bfs(encoding): Creates a tree from the provided encoding using breadth-first search.
        encode_bfs(): Encodes the tree in breadth-first order.
        insert_children(dep): Inserts children nodes into the tree based on the dependency string.
        insert_node_bfs(nn): Inserts a new node into the tree using breadth-first search.

    Attributes:
        root: The root node of the binary tree.

    Assumptions:
        Node values are unique.

    Example Usage:
        tree = Tree(root_node)
        new_node = Node(value)
        tree.insert_node_bfs(new_node)
    '''
    def __init__(self, root: 'Node') -> None:
        '''
        Initializes a new instance of the Tree class.

        Args:
            root: The root node of the binary tree.

        Example Usage:
            tree = Tree(root_node)
        '''        '''
        Initializes a new instance of the Tree class.

        Args:
            root: The root node of the binary tree.
        '''
        self.root = root

    @classmethod
    def from_encoding_bfs(cls, encoding: List[str]) -> 'Tree':
        '''
        Creates a tree from the provided encoding using breadth-first search.

        The encoding should be a list of strings, where each string represents 
        a node in the format: 'value: (left_value, right_value)'.
        The method creates a tree with the encoded nodes and returns a new Tree 
        instance.

        Args:
            encoding: The list of strings representing the nodes in breadth-first order.

        Returns:
            A new Tree instance created from the provided encoding.

        Example Usage:
            encoding = ['1: (2, 3)', '2: (4, 5)', '3: (6, 7)']
            tree = Tree.from_encoding_bfs(encoding)
        '''
        # create root
        pattern =r'(\d+): \((\d+), (\d+)\)'
        root_val = int(re.match(pattern,encoding[0]).group(1))
        root = Node(root_val)
        tree = Tree(root)

        # populate tree
        for dep in encoding:
            tree.insert_children(dep)

        return cls(root) 

    def encode_bfs(self) -> List[str]:
        '''
        Encodes the tree in breadth-first order.

        Returns a list of string representations of each node in the tree, 
        encoded in breadth-first order.

        Complexity:
            CPU O(N)
            MEM O(N)

        Returns:
            A list of string representations of nodes in the tree, encoded 
            in breadth-first order.

        Example Usage:
            tree = Tree(root_node)
            encoded_tree = tree.encode_bfs()
        '''
        return [str(node) for node in BFS_iter(self)]

    def insert_children(self, dep: str) -> None:
        '''
        Inserts children nodes into the tree based on the dependency string.

        The dependency string follows the format: 
        'parent_value: (child_left_value, child_right_value)'.

        Args:
            dep: The dependency string representing the parent and children nodes.

        Returns:
            None.

        Example Usage:
            tree = Tree(root_node)
            tree.insert_children('1: (2, 3)')
        '''        # decode parent, child left, child right values
        pattern = r'(\d+): \((\d+), (\d+)\)'
        parent_val = int(re.match(pattern,dep).group(1))
        child_left_val = int(re.match(pattern,dep).group(2))
        child_right_val = int(re.match(pattern,dep).group(3))
        # find parent in tree
        for node in BFS_iter(self):
            if node.value == parent_val:
                # insert left child
                if child_left_val > 0:
                    child_left = Node(child_left_val)
                    node.left = child_left
                # insert right child
                if child_right_val > 0:
                    child_right = Node(child_right_val)
                    node.right = child_right

    def insert_node_bfs(self, nn: 'Node') -> bool:
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
            True if the node is successfully inserted, NodeInsertionError otherwise.

        Example Usage:
            tree = Tree(root_node)
            new_node = Node(value)
            tree.insert_node_bfs(new_node)
        '''
        for node in BFS_iter(self):
            if node.left is None:
                node.left = nn
                return True
            elif node.right is None:
                node.right = nn
                return True

    def split_root(self) -> List['Tree']:
        '''
        Splits the current tree's root into left and right subtrees.

        Returns:
            A list of subtrees after splitting the root.

        Raises:
            None.

        Example:
            tree = Tree(root)
            subtrees = tree.split_root()
        '''
        subtrees = []
        if self.root.left is not None:
            t1 = Tree(self.root.left)
            t1_enc = t1.encode_bfs()
            t1 = Tree.from_encoding_bfs(t1_enc)
            subtrees.append(t1)
        if self.root.right is not None:
            t2 = Tree(self.root.right)
            t2_enc = t2.encode_bfs()
            t2 = Tree.from_encoding_bfs(t2_enc)
            subtrees.append(t2)
        return subtrees



