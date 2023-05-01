from ipdb import set_trace
import operator

from galois_field import GaloisField
from vector import Vector, BinVector



# Create GF2 field
F = [0,1]
add_op = operator.xor
mul_op = operator.and_
add_id = 0
mul_id = 1
add_inv_op = lambda a: a
mul_inv_op = lambda a: a

field = GaloisField(F=F, add_op=add_op, mul_op=mul_op,
        add_id = add_id, mul_id=mul_id,
        add_inv_op=add_inv_op, mul_inv_op=mul_inv_op)

field.validate()

# create vector addition over GF2 field
v1 = Vector([3,3])
v2 = Vector([4,4])
v3 = Vector([5,5])

b1 = BinVector(3, field)
b2 = BinVector(4, field)
b3 = BinVector(5, field)


set_trace()
v_sum = v1+v2+v3
b_sum = b1+b2+b3


set_trace()
print('fin')
