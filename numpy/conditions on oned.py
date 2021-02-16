import numpy as nm
a=nm.arange(10)

#extracting odd position values
a=a[a%2==1]
print(a)

#even position
a=nm.arange(10)

a=a[a%2==0]
print(a)

#replacing odd values with 1
a=nm.arange(10)
a[a%2==1]=1
print(a)

#replace values without affecting origional array by where function
print(nm.where(a%2==1,a,15))
print(a)
