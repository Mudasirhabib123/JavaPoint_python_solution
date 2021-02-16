import numpy as nm
p=nm.array([1,2,3])
#repeating each element
print(nm.repeat(p,3))

#repeating whole array

print(nm.tile(p,3))

#repeating each element and whole array
a=nm.r_[nm.repeat(p,4),nm.tile(p,3)]
print(a)
