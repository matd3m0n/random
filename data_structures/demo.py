from ipdb import set_trace

from binary_tree.node import Node
from binary_tree.tree import Tree
from binary_tree.iterators import BFS_iter, DFS_iter

# create a binary tree
root = Node(1)
tree = Tree(root)
for i in range(2,18):
    tree.insert_node_bfs(Node(i))

# traverse using BFS and DFS
print('print nodes in BFS fashion')
for node in BFS_iter(tree):
    print('\t', node)

print('print nodes in DFS fashion')
for node in DFS_iter(tree):
    print('\t', node)

# encode and decode a tree
encoding = tree.encode_bfs()
print('Tree encoding: ', encoding) 
set_trace()
t2 = Tree.from_encoding_bfs(encoding)

set_trace()
print('fin')
