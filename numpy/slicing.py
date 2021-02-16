import numpy as nm
a=nm.array([(1,2,3,4),(5,6,7,8)])
print(a)
#slicing
#printing first row
print(a[0,:4])

#printing 2nd row
print(a[1:2,:4])

#printing row
print(a[:2,:1])
#printing two mid rows
print(a[:2,2:4])
