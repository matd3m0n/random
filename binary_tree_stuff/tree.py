from ipdb import set_trace
from iterators import BFS_iter

class Tree:
    def __init__(self, root):
        self.root = root

    def insert_node(self, nn):
        for node in BFS_iter(self):
            if node.left is None:
                node.left = nn
                return True
            elif node.right is None:
                node.right = nn
                return True


