def ishappy(n):
	nmb=0
	while(n>0):
		d=n%10
		nmb+=d**2
		n//=10
	return nmb

for i in range(1,101):
	nm=res=i
	while(res!=1 and res!= 4):
		res=ishappy(res)
	if (res==1):
		print(i)

