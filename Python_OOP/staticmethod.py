class employee:
	def __init__(self,name,age,salary):
		self.name=name
		self.age=age
		self.salary=salary
	@staticmethod
	def isemp(nmb):
		if (nmb in range(1,100)):
			return "employee"
		else:
			return "Fake"
ali=employee("Ali Ahmad",23,40000)
check=employee.isemp(10)
print(check)
