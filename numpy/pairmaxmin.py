def max(x,y):
    if(x>y):
        return x
    else:
        return y

import numpy as nm
maxx=nm.vectorize(max,otypes=[int])
a=nm.random.randint(10,40,10)
b=nm.random.randint(8,40,10)
print(a)
print(b)

print(maxx(a,b))
