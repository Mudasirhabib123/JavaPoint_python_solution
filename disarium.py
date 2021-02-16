n=int(input("Enter any value"))
temp=n
d=sum=0
while(temp!=0):
	temp//=10
	d+=1
temp=n
while(temp!=0):
	c=temp%10
	sum+=(c**d)
	d-=1
	temp//=10
if(sum == n):
	print(f"number {n} is disarium")
else:
	print("not disarium")
