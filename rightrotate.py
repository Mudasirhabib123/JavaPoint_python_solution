a=[1,2,3,4,5,6]
t=a[len(a)-1]

for i in range(len(a)-1,-1,-1):
	a[i]=a[i-1]
a[0]=t

print(a)
