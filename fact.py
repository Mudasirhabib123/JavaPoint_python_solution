nmb=int(input("Enter any nmb"))
f=1
for i in range(1,nmb):
	f=(f*i)+f
print(f"Factorial of {nmb} is {f}")
