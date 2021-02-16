import numpy as nm
a=nm.array([(1,2,3,4),(5,6,7,8)])
print(a)
b=nm.array([(10,20,30,40),(5,6,7,8)])
print(b)

#horizently stack
c=nm.hstack((a,b))
print(c)

#verticaly stack
print()
print(nm.vstack((a,b)))

print(a.ravel())
