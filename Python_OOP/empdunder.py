class employee:
	def __init__(self,n,s):
		self.name=n
		self.salary=s
	def __add__(first,secnd):
		return first.salary + secnd.salary


ali=employee("ali",20000)
saad=employee("saad",15000)
print(saad + ali)
