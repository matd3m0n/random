#from bit_builder import BitBuilder
from ipdb import set_trace

class Bit:
    def __init__(self):
        self.ar = None 

    def __str__(self):
        return str(self.ar)

    def __len__(self):
        return len(self.ar)
    
    def __eq__(self, b2):
        self.unpad()
        b2.unpad()
        return True if self.ar == b2.ar else False

    def get_bit(self, i) -> bool:
        return self.ar[i]

    def set_bit(self,i):
        self.ar[i] = 1

    def clear_bit(self,i):
        self.ar[i] = 0

    def update_bit(self, i, dig):
        self.ar[i] = dig


    def all_0(self):
        new_ar = [0,]*len(self)
        return Bit.from_ar(new_ar)

    def all_1(self):
        new_ar = [1,]*len(self)
        return Bit.from_ar(new_ar)

    def copy(self):
        return Bit.from_ar(self.ar)

    def __mul__(self, b2):
        def mul_by_digit(b1, digit):
            if digit == 1:
                return self.copy()
            else:
                return self.all_0()

        new_bit = Bit.from_ar([0])

        for k, dig in enumerate(b2.ar[::-1]):
            tmp = mul_by_digit(self, dig)
            new_bit = new_bit + (tmp << k)

        return new_bit

    def __or__(self, b2):
        self.pad(b2)
        b2.pad(self)

        new_ar = []
        for d1,d2 in zip(self.ar, b2.ar):
            new_ar.append(1*(d1+d2>=1))
        return Bit.from_ar(new_ar)
     
    def __and__(self, b2):

        self.pad(b2)
        b2.pad(self)

        new_ar = []
        for d1,d2 in zip(self.ar, b2.ar):
            new_ar.append(d1*d2)
        return Bit.from_ar(new_ar)
        

    def __rshift__(self, k): # logical right shift
        new_ar = [0,]*k+self.ar
        for i in range(k):
            new_ar.pop(-1)
        return Bit.from_ar(new_ar)

    def __lshift__(self, k):
        new_ar = self.ar.copy()
        for i in range(k):
            new_ar.append(0)
        return Bit.from_ar(new_ar)

    def __add__(self, b2):
        def add_dig(tup1,tup2): # tup = digit, carry
            tup3 = [0,0]
            # add digits
            tup3[0] = tup1[0]+tup2[0]
            if tup3[0]==2:
                tup3[0] = 0
                tup3[1] = 1
            # add carry
            if tup1[1]+tup2[1] > 0:
                tup3[0]+=1
                if tup3[0]==2:
                    tup3[0] = 0
                    tup3[1] = 1
            return tup3

        self.pad(b2)
        b2.pad(self)

        new_ar = []

        carry = 0
        for dig1, dig2 in zip(self.ar[::-1], b2.ar[::-1]):
            dig1 = dig1,carry
            dig2 = dig2,0
            c_sum = add_dig(dig1,dig2)
            new_ar.insert(0, c_sum[0])
            carry = c_sum[1]

        if carry==1:
            new_ar.insert(0,1)
        new_bit = Bit.from_ar(new_ar)
        return new_bit

    def __xor__(self, b2):
        def bitwise_xor(d1,d2):
            return 1 if d1+d2==1 else 0


        self.pad(b2)
        b2.pad(self)

        new_ar = []
        for d1,d2 in zip(self.ar, b2.ar):
            new_ar.append(bitwise_xor(d1,d2))

        return Bit.from_ar(new_ar)

    def neg(self):
        new_ar = []
        for dig in self.ar:
            new_ar.append(1-dig)

        return Bit.from_ar(new_ar)

    @classmethod
    def from_int(cls, k):
        bit = cls()
        bit.ar = list(map(int, list(bin(k)[2:])))

        return bit
    
    @classmethod
    def from_ar(cls, ar):
        bit = Bit()
        bit.ar = ar
        return bit

    @classmethod
    def from_str(cls, s):
        if s.startswith('0b'):
            s = s[2:]
        bit = Bit()
        bit.ar = list(map(int, list(s)))
        return bit

    def pad(self, b2): # inplace
        while len(self) < len(b2):
            self.ar.insert(0, 0)

    def unpad(self): # inplace        
        while self.ar[0] == 0 and len(self)>=2:
            self.ar.pop(0)


    def to_int(self):
        return int(''.join(list(map(str, self.ar))), 2)

