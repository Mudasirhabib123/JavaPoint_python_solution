s,e=input("enter starting and ending nmb ").split()
st=int(s)
end=int(e)


while st<=end:
	a=2
	while a<=st:
		if st%a == 0:
			break
		a+=1
	if a==st:
		print(st)
	st+=1
