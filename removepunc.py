pun=".,/<>?\":';[]\=-_+~`!@#$%^&*()"
str=input("Enter any string")
str2=""
for i in str:
	if(i not in pun):
		str2+=i

print(str2)
