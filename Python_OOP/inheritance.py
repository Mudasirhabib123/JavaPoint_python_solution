class Man:
	def __init__(self,name,age):
		self.name=name
		self.age=age

class Employee(Man):
	def __init__(self,name,age,salary,empno):
		super().__init__(name,age)
		self.salary=salary
		self.empno=empno

class Programmer(Employee):
	def __init__(self,name,age,salary,empno,plang,exp):
		super().__init__(name,age,salary,empno)
		self.plang=plang
		self.exp=exp






class Manager(Man,Employee):
	pass


ali=Programmer("ali ahmad",22,35000,12,"python","5 years")
print(ali.name)

saad=Manager("saad",34,40000,10,)
print(saad.name)


#print(dir(Man))
