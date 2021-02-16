a=[
[1,2,3,4],
[5,6,7,8]
]

tr=[
[0,0],
[0,0],
[0,0],
[0,0]
]


for i in range(len(a)):
	for j in range(len(a[0])):
		tr[j][i]=a[i][j]

print(tr)
