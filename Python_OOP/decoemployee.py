class employee:
	total=0
	incr=5000


	def __init__(self,fname,lname,salary):
                self.fname=fname
                self.lname=lname
                self.salary=salary
                employee.total+=1

	def increase (self):
		self.salary=self.salary+self.incr


	def __del__(self):
		employee.total-=1
	#creating decorator
	@classmethod
	def changeincr(cls,val):
		cls.incr=val


ali=employee("Ali ","Ahmad",20000)
saad=employee("saad","ali",25000)

print(ali.fname,ali.lname,ali.salary)
print(saad.fname, saad.lname,saad.salary)

ali.increase()
print(ali.salary)
print("total Employees are",employee.total)

del ali

print("total Employees are",employee.total)

print(employee.incr)
employee.changeincr(10000)
print(employee.incr)

