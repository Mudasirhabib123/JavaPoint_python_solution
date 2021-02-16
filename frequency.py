a=[1,2,3,2,3,4,5,1,6]
print(a)
t=a
fr=[0]*len(a)
for i in range(len(a)):
	for j in range(i,len(a)):
		if(a[i]==a[j]):
			fr[i]+=1

for i in range(len(a)):
	print(f"frequency of {i} element is{fr[i]}")
