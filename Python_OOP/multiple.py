class square:
	def calculate(a,b):
		return a*a,b*b


a=5
b=6
a,b=square.calculate(a,b)
print(a,b)
