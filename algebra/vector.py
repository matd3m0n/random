from typing import Optional

class Vector:
    '''
    Represents a vector.

    A vector is a mathematical object that represents an ordered list of elements.

    Attributes:
        ar (list): The list of elements representing the vector.
        F (list, optional): A field over which vector operations should be 
        performed. Defaults to R.
    '''
    def __init__(self, ar: list, F: Optional['Field'] = None):
        '''
        Initializes a Vector.

        Args:
            ar (list): The list of elements representing the vector.
            F (Field, optional): A field over which vector operations should 
            be performed. Defaults to R.
        '''
        self.ar = ar
        self.F = F

    def __str__(self) -> str:
        '''
        Returns:
            str: The string representation of the vector.
        '''
        return str(self.ar)

    def __len__(self) -> int:
        '''
        Returns:
            int: The length of the vector.
        '''
        return len(self.ar)

    def __add__(self, v2: 'Vector') -> 'Vector':
        '''
        Adds two vectors element-wise or field R.

        Args:
            v2 (Vector): The vector to be added.

        Returns:
            Vector: The resulting vector after element-wise addition.
        '''
        v_sum = []
        # add over field F
        assert self.F is None # vector addition over R
        for el1, el2 in zip(self.ar, v2.ar):
            v_sum.append(el1 + el2)
        # construct new vector
        new_v = Vector(v_sum, self.F)
        return new_v
 

class BinVector(Vector):
    '''
    Represents a binary vector, which is a subclass of the Vector class.

    A binary vector is a vector where each element is a binary digit (0 or 1).

    Attributes:
        ar (list): The list of elements representing the vector.
        F (Field): A field (such as Galois Field) over which vector operations 
        should be performed.
    '''
    def __init__(self, nr: int, F: 'Field'):
        '''
        Initializes a Binary Vector.

        Args:
            nr (int): The decimal representation of the binary vector.
            F : A Field (such as Galois Field) over which vector operations 
            should be performed.
        '''
        # transform all numbers to binary strings
        bin_v = list(map(int, bin(nr)[2:]))
        super().__init__(bin_v, F)  # Call the superclass constructor

    def __add__(self, v2: 'BinVector') -> 'BinVector':
        '''
        Adds two binary vectors element-wise over field F.

        Args:
            v2 (BinVector): The binary vector to be added.

        Returns:
            BinVector: The resulting binary vector after element-wise addition.
        '''
        # pad shorter vector with 0
        while len(v2) < len(self):
            v2.ar.insert(0, 0)
        while len(self) < len(v2):
            self.ar.insert(0, 0)

        v_sum = []    
        for el1, el2 in zip(self.ar, v2.ar):
            v_sum.append(self.F.add(el1, el2))

        # transform binary vsum to actual nr
        nr = int(''.join(map(str, v_sum)), 2)

        new_v = BinVector(nr, self.F)
        return new_v
 
    def __str__(self) -> str:
        '''
        Returns the string representation of the binary vector.

        Returns:
            str: The string representation of the binary vector.
        '''
        return '%s (ie %d)'%(str(self.ar), int(''.join(map(str, self.ar)), 2))
        
    def decode(self) -> int:
        '''
        Returns:
            int: The decimal representation of the binary vector.
        '''
        return int(''.join(map(str, self.ar)), 2)

