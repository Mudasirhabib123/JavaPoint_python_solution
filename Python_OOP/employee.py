class employee:
	total=0
	"""documentation about employe"""
	def __init__(self,fname,lname,salary):
		self.fname=fname
		self.lname=lname
		self.salary=salary
		employee.total+=1

	def increase (self,incr):
		self.salary=self.salary+incr

	def __del__(self):
		employee.total-=1


ali=employee("Ali ","Ahmad",20000)
saad=employee("saad","ali",25000)

print(ali.fname,ali.lname,ali.salary)
print(saad.fname, saad.lname,saad.salary)
ali.increase(15000)
print(ali.increase(12000))
print("total Employees are",employee.total)

del ali

print("total Employees are",employee.total)

print(getattr(saad,"fname"))
setattr(saad,"salary",43000)
print(getattr(saad,"salary"))

print(hasattr(saad,"name"))

#delattr(saad,"lname")
print(hasattr(saad,"lname"))

print(saad.__dict__)
print(employee.__doc__)

print(saad.__module__)
print(employee.__name__)
print(employee.__bases__)
