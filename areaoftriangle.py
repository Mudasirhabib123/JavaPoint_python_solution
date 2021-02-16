a=int(input("Enter first side of triangle"))
b=int(input("enter seccond side of triangle"))
c=int (input("enter third side"))
s=(a+b+c)*0.5
a=(s*(a-b)+s*(a-c))
print("area of triangle is",a)
