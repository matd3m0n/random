from ipdb import set_trace
from stack import Stack

        
class BFS_iter:
    '''
    The BFS_iter class represents an iterator for traversing a binary tree 
    using breadth-first search (BFS) algorithm.

    It performs a level-by-level traversal of the tree, visiting the nodes in 
    breadth-first order.

    Methods:
        __init__(tree): Initializes a new instance of the BFS_iter class.
        __iter__(): Returns the iterator object itself.
        __next__(): Retrieves the next node in the breadth-first order traversal.

    Attributes:
        root: The root node of the binary tree.

    CPU time:
        O(N) - we are visiting all nodes once
    
    MEM:
        O(N/2 + N/4) - We will have at most N/2 +N/4 children in the list


    Example Usage:
        tree = BinarySearchTree()
        # Populate the tree with nodes

        bfs_iterator = BFS_iter(tree)
        for node in bfs_iterator:
            # Process each node in breadth-first order
            print(node)
    '''
    def __init__(self, tree: 'Tree') -> None:
        '''
        Initializes a new instance of the BFS_iter class.

        Args:
            tree: The binary tree for traversal.
        '''
        self.root = tree.root

    def __iter__(self) -> 'BFS_iter':
        '''
        Returns the iterator object itself.

        Returns:
            The iterator object.
        '''
        self.c_index = 0
        self.children = [self.root]
        return self
        
    def __next__(self) -> 'Node':
        '''
        Retrieves the next node in the breadth-first order traversal.

        Returns:
            The next node in the breadth-first order traversal.

        Raises:
            StopIteration: If there are no more nodes to traverse.
        '''
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
            if len(gc) == 0:
                raise StopIteration
            self.children = gc
            self.c_index = 0
            current_element = self.children[self.c_index]
            self.c_index += 1
            return current_element


class DFS_iter:
    '''
    The DFS_iter class represents an iterator for traversing a binary tree 
    using depth-first search (DFS) algorithm.

    It performs a depth-first traversal of the tree, visiting the nodes in a 
    pre-order traversal.

    Methods:
        __init__(tree): Initializes a new instance of the DFS_iter class.
        __iter__(): Returns the iterator object itself.
        __next__(): Retrieves the next node in the depth-first order traversal.

    Attributes:
        root: The root node of the binary tree.

    CPU time:
        O(3N) - Visiting each node 3 times (leaves 2 times)
    
    MEM:
        O(log(N)) + O(N) - log(N) of stack + N visited nodes

    Example Usage:
        tree = BinarySearchTree()
        # Populate the tree with nodes

        dfs_iterator = DFS_iter(tree)
        for node in dfs_iterator:
            # Process each node in depth-first order
            print(node)

    '''
    def __init__(self, tree: 'Tree') -> None:
        '''
        Initializes a new instance of the DFS_iter class.

        Args:
            tree: The binary tree for traversal.
        '''
        self.root = tree.root

    def __iter__(self) -> 'DFS_iter':
        '''
        Returns the iterator object itself.

        Returns:
            The iterator object.
        '''
        self.visited = {}
        self.st = Stack()
        self.st.insert(self.root)
        return self
 
    def __next__(self) -> 'Node':
        '''
        Retrieves the next node in the depth-first order traversal.

        Returns:
            The next node in the depth-first order traversal.

        Raises:
            StopIteration: If there are no more nodes to traverse.
        '''
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

