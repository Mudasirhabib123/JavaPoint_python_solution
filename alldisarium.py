def len(n):
	l=0
	while(n!=0):
		l+=1
		n//=10
	return l
for i in range(1,101):
	temp=i
	l=len(temp)
	s=0
	while(temp!= 0):
		d=temp%10
		s+=(d**l)
		l-=1
		temp//=10
	if(s==i):
		print(i)
