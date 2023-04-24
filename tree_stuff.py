from ipdb import set_trace

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
    def __init__(self):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass


root = Node(666)
tree = Tree(root)
set_trace()
for i in range(1,10):
    tree.insert_node(Node(i))


set_trace()

