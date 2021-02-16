import numpy as nm
a=nm.array([1,2,3,4,5,6])
print(a)

a=nm.arange(10)
print(a)

a=nm.arange(10,50,3)
print(a)

a=nm.arange(9).reshape(3,3)
print(a)
a=nm.zeros(10)
print(a)

a=nm.ones(10)
print(a)

a=nm.ones((3,3),dtype=bool)
print(a)

#creating two dimension numpy array
a=nm.array([(1,2,3),(4,5,6)])
print(a)
print(a.ndim)

a=nm.arange(50,60)
print(a)
print(a.ndim)

a=nm.full((3,4),True,dtype=bool)
print(a)

a=nm.full((2,3),1,dtype=bool)
print(a)

a=nm.empty(5)
print(a)

#creating array with random values

a=nm.random.randint(10,50,10,int)
print(a)
