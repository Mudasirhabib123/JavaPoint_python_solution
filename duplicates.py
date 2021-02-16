a=[1,2,3,4,2,3,1,5,6,7,8,6,7,6]
for i in range(len(a)):
	for j in range(i+1,len(a)):
		if(a[i]==a[j]):
			print(i)
