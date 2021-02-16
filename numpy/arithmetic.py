import numpy as nm
a=nm.arange(1,20,2)
print(a)

print(f"Minimum in array is {min(a)}")

print(f"Maximum in array is {max(a)}")

print(f"mean of array is {nm.mean(a)}")

print(f"product of array is {nm.prod(a)}")

print(f"sum of array is {sum(a)}")

print(f"varient of array is {nm.var(a)}")

print(f"index of min  in array is {nm.argmin(a)}")

print(f"index of max in array is {nm.argmax(a)}")

print(f"square root of array is {nm.sqrt(a)}")

print(f"standard daviation of array is {nm.std(a)}")



#on multi dimensions array
#printing the sum of columns
a=nm.array([(1,2,3),(4,5,6)])

print(a.sum(axis=0))

#printing the sum of rows

print(a.sum(axis=1))


b=nm.array([(1,2,3),(4,5,6)])

#printing addition of two arrays

print(a+b)
print(a-b)
print(a*b)
print(a/b)
