a,b=input("Enter two values").split()
a,b=int(a),int(b)
if(a>b):
	g=a
else:
	g=b
while(1):
	if(g%a == 0 and g%b == 0):
		break
	else:
		g+=1
print(f"lcm of {a} and {b} is= {g}")
