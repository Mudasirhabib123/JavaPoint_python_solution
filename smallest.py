a=[1,2,3,4,2,3,4,5,7]
s=a[0]
for i in range(len(a)):
	if(a[i]<s):
		s=a[i]

print(s)
