nmb=int(input("Enter any nmb"))
arm=0
num=nmb
while nmb>0:
	d=nmb%10
	arm+=d**3
	nmb=nmb//10
if num==arm:
	print("Number is armstrong")
else:
	print("Number is not armstrong")
