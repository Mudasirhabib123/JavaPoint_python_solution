a=[1,2,3,4,5]
t=a[0]
for i in range(len(a)-1):
	a[i]=a[i+1]

a[len(a)-1]=t
print(a)
