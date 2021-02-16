def hcf(a,b):
	if(a>b):
		l=b
	else:
		l=a
	while(1):
		if(a%l==0 and b%l == 0):
			break
		else:
			l-=1
	if(l>1):
		print(f"HCF of {a} and {b} is \t={l}")

none=int(input("Enter aqny nmb"))
ntwo=int(input("Enter 2nd nmb"))
hcf(none,ntwo)
