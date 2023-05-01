'''
Based on:
    https://en.wikipedia.org/wiki/Finite_field
'''

class GaloisField:
    '''
    Represents a Galois Field.

    A Galois Field is a field that consists of a finite set 
    of elements along with two operations: addition and multiplication.

    Attributes:
        F (list): The finite field elements.
        add (callable): Addition operation.
        mul (callable): Multiplication operation.
        add_id: Additive identity element.
        mul_id: Multiplicative identity element.
        add_inv_op (callable): Additive inverse operation.
        mul_inv_op (callable): Multiplicative inverse operation.
    '''
    def __init__(self, F: list, add_op: callable, mul_op: callable,
            add_id: object, mul_id: object,
            add_inv_op: callable, mul_inv_op: callable):
        '''
        Initializes a Galois Field.

        Args:
            F (list): The finite field elements.
            add_op (callable): Addition operation.
            mul_op (callable): Multiplication operation.
            add_id: Additive identity element.
            mul_id: Multiplicative identity element.
            add_inv_op (callable): Additive inverse operation.
            mul_inv_op (callable): Multiplicative inverse operation.
        '''
        self.F = F
        self.add = add_op
        self.mul = mul_op
        self.add_id = add_id # 0
        self.mul_id = mul_id # 1
        self.add_inv_op = add_inv_op # -a
        self.mul_inv_op = mul_inv_op # 1/a

    def validate(self) -> int:
        '''
        Validates if the given Galois Field satisfies the properties of a Galois Field.

        Returns:
            int: 1 if it is a Galois Field, 0 otherwise.
        '''
        def val_finite(self):
            assert len(self.F) < 10**10, 'finite F failed'

        def val_additive_associativity(self): # a+(b+c) = (a+b)+c  
            for a in self.F:
                for b in self.F:
                    for c in self.F:
                        assert self.add(a, self.add(b,c))\
                            == self.add(self.add(a,b), c),\
                            'additive assocativity failed'

        def val_multiplicative_associativity(self): # a(bc) = (ab)c  
            for a in self.F:
                for b in self.F:
                    for c in self.F:
                        assert self.mul(a, self.mul(b,c))\
                            == self.mul(self.mul(a,b), c),\
                            'multiplicative associativity failed'

        def val_additive_commutativity(self): # a+b = b+a 
            for a in self.F:
                for b in self.F:
                    assert self.add(a,b) == self.add(b,a),\
                    'additive commutativity failed'

        def val_multiplicative_commutativity(self): # ab = ba
            for a in self.F:
                for b in self.F:
                    assert self.mul(a,b) == self.mul(b,a),\
                    'multiplicative commutativity failed'

        def val_additive_identity(self): # exists 0 st a+0=a for all a
            for a in self.F:
                assert self.add(a, self.add_id) == a,\
                'additive identity failed'

        def val_multiplicative_identity(self): # exists 1 st a*1 = a
            for a in self.F:
                assert self.mul(a, self.mul_id) == a,\
                'multiplicative identity failed'

        def val_additive_inverse(self): # for all a exists -a st a+(-a) = 0
            for a in self.F:
                assert self.add(a, self.add_inv_op(a)) == self.add_id,\
                'additive inverse failed'

        def val_multiplicative_inverse(self): # for all a!=0 exists 1/a st a * 1/a = 1
            for a in self.F:
                if a != self.add_id:
                    assert self.mul(a, self.mul_inv_op(a)) == self.mul_id,\
                    'multiplicative inverse failed'

        def val_distributivity(self): # a(b+c) = ab + ac
            for a in self.F:
                for b in self.F:
                    for c in self.F:
                        assert self.mul(a, self.add(b,c))\
                            == self.add(self.mul(a,b), self.mul(a,c)),\
                            'distributivity failed'

        try:
            val_finite(self)
            val_additive_associativity(self)
            val_multiplicative_associativity(self)
            val_additive_commutativity(self)
            val_multiplicative_commutativity(self)
            val_additive_identity(self)
            val_multiplicative_identity(self)
            val_multiplicative_identity(self)
            val_multiplicative_identity(self)
            val_distributivity(self)
        except AssertionError as e:
            print('Not a Galois Field: ', str(e))
            return 0
        else:
            print('It is a Galois Field')
            return 1



            

