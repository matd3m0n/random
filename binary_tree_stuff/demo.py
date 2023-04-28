from ipdb import set_trace

from node import Node
from tree import Tree
from iterators import BFS_iter, DFS_iter

# create a binary tree
root = Node(1)
tree = Tree(root)
for i in range(2,16):
    tree.insert_node(Node(i))

print('print nodes in BFS fashion')
for node in BFS_iter(tree):
    print('\t', node)

print('print nodes in DFS fashion')
for node in DFS_iter(tree):
    print('\t', node)

 

set_trace()
print('fin')
