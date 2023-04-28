'''
Simple binary tree implementation with:
    Breadh First Search
    Depth First Search
'''
from ipdb import set_trace

class Stack:
    def __init__(self):
        self.stack = []

    def insert(self, el):
        self.stack.append(el)

    def pop(self):
        return self.stack.pop(-1)

    def peek(self):
        return self.stack[-1]
        
class Node:
    ''' node in a binary tree '''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        tl = 0 if self.left is None else self.left.value
        tr = 0 if self.right is None else self.right.value
        return '%d: (%d, %d)'%(self.value, tl, tr)

    def get_children(self):
        children = [child for child in [self.left, self.right]\
                if child is not None]
        return children

    def is_leaf(self):
        return True if self.left is None and self.right is None else False

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
            
class BFS_iter:
    def __init__(self, tree):
        self.root = tree.root

    def __iter__(self):
        self.c_index = 0
        self.children = [self.root]
        return self
        
    def __next__(self):
        if len(self.children) == 0:
            raise StopIteration
        if self.c_index < len(self.children):
            current_element = self.children[self.c_index]
            self.c_index += 1
            return current_element
        else: # go deeper 
            gc = []
            for child in self.children:
                gc += child.get_children()
            self.children = gc
            self.c_index = 0
            current_element = self.children[self.c_index]
            self.c_index += 1
            return current_element


class DFS_iter:
    ''' 
    Issues:
        O(N) of extra space (visited)
        O(log(N)) extra space of stack
        checks is_visited() multiple times for same node 
    '''
    def __init__(self, tree):
        self.root = tree.root

    def __iter__(self):
        self.visited = {}
        self.st = Stack()
        self.st.insert(self.root)
        return self
 
    def __next__(self):
        if len(self.st.stack) == 0:
            raise StopIteration
        node = self.st.peek()
        if node.is_leaf():
            self.st.pop()
            return self.__next__()
        # go center
        if node not in self.visited:
            self.visited[node] = True
            return node
        # go left
        left = node.left
        if left not in self.visited:
            self.st.insert(left)
            self.visited[left] = True
            return left
        # go right
        right = node.right
        if right not in self.visited:
            self.st.insert(right)
            self.visited[right] = True
            return right
        # go up
        self.st.pop()
        return self.__next__()

root = Node(1)
tree = Tree(root)
for i in range(2,4):
    tree.insert_node(Node(i))
set_trace()

for el in DFS_iter(tree):
    print(el)

set_trace()

