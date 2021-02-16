n=int(input("Enter any nmb"))
s=0
t=n
while(t!= 0):
	d=t%10
	s+=d
	t//=10

if(n%s==0 ):
	print(n,"is harshard nmb")
else:
	print(n," is not harshard nmb")
