def fibnoci(n):
	if(n<=1):
		return n
	else:
		return (fibnoci(n-1)+fibnoci(n-2))
n=int(input("Enter any nmb"))
if(n<1):
	print("input greater than 1 nmb")
else:
	for i in range(n):
		print(fibnoci(i))
