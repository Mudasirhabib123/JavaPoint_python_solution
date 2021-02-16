import cmath
a=float(input("Enter a"))
b=float(input("enter b"))
c=float(input("Enter c"))
d=(b**2)-(4*a*c)
nfact=((-b)-cmath.sqrt(d))/(2*a)
pfact=((-b)+cmath.sqrt(d))/(2*a)
print(f" Negative factor is {nfact}")
print(f"Positive factor is {pfact}")
