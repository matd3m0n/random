class Stack:
    '''
    The Stack class represents a stack data structure.

    A stack follows the Last-In-First-Out (LIFO) principle, where the last 
    element inserted is the first one to be removed.
    This implementation of a stack uses a list as its underlying data structure.

    Methods:
        __init__(): Initializes a new instance of the Stack class.
        insert(el): Inserts an element at the top of the stack.
        pop(): Removes and returns the element at the top of the stack.
        peek(): Returns the element at the top of the stack without removing it.
    '''
    def __init__(self):
        '''
        Initializes a new instance of the Stack class.

        The stack is implemented using a list.
        '''
        self.stack = []

    def insert(self, el): # O(1)
        '''
        Inserts an element at the top of the stack.

        Args:
            el: The element to be inserted.
        '''
        self.stack.append(el)

    def pop(self): # O(1)
        '''
        Removes and returns the element at the top of the stack.

        Returns:
            The element at the top of the stack.
        '''
        return self.stack.pop(-1)

    def peek(self): # O(1)
        '''
        Returns the element at the top of the stack without removing it.

        Returns:
            The element at the top of the stack.
        '''
        return self.stack[-1]
        

