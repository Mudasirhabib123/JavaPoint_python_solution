str=int(input("Enter any starting nmb"))
end=int(input("Enter ending nmb"))


while(str<=end):
	for i in range(1,str):
		if(str==(i*(i+1))):
			print(str)

	str+=1
