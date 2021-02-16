a=[1,2,3,4,5,6,7]
l=a[0]
for i in range(len(a)):
	if(a[i]>l):
		l=a[i]


print(f"largest element in array is {l}")
