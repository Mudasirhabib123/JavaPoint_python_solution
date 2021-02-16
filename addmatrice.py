a=[
[1,2,3],
[4,5,6],
[7,8,9]
]
b=[
[12,13,14],
[3,2,4],
[5,2,3]
]

c=[
[0,0,0],
[0,0,0],
[0,0,0]
]
for i in range(len(a)):
	for j in range(len(a)):
		c[i][j]=a[i][j]+b[i][j]

for i in range(len(a)):
	for j in range(len(a)):
		print(c[i][j])
