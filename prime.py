n=int(input("Enter any nmb"))
if(n<2):
	print("nmb must be greater than 1")
else:
	i=2
	while(i<n):
		if (n%i==0):
			break
		i+=1
if(n>i):
	print(f"{n} is not prime nmb")
else:
	print(f"{n} nmb is prime nmb")
