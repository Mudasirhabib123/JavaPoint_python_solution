def ishappy(n):
	if(n<1):
		return n
	else:
		s=0
		while(n>0):
			d=n%10
			s+=d*d
			n//=10
	return s

n=int(input("Enter any number"))
res=n
while(res != 1 and res != 4):
	res=ishappy(res)

if (res == 1):
	print(f"{n} is happy nmb")
else:
	print(f"{n} is not happy")
