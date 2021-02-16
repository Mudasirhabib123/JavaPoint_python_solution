a=[1,3,2,4,5,64,23,67,89,43,1,23]
for i in range(len(a)):
	for j in range(i,len(a)):
		if(a[i]<a[j]):
			temp=a[i]
			a[i]=a[j]
			a[j]=temp

print(a)
