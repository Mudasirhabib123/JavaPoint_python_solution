a=0
b=1
c=a+b
terms=int(input("ente terms nmb"))
if(terms==0):
	print("0")
elif(terms== 1):
	print("0\t 1")
else:
	print("0 \t 1")
	i=2
	while(i<terms):
		print("\t",c)
		a=b
		b=c
		c=a+b
		i+=1
