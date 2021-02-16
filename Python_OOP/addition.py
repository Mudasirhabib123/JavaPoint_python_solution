#Parrent class Man
class Man:
	def __init__(self,n,age,nat):
		self.name=n
		self.__age=age
		self.nationality=nat

	def changeage(self,age):
		self.__age=age

	def printage(self):
		print(self.__age)

#Child class Employee
class Employee(Man):
	def __init__(self,n,age,nat,sal,gr,exp):
		super(). __init__(n,age,nat)
		self.__salary=sal
		self._grade=gr
		self.experience=exp


	@classmethod
	def empstr(cls,str):
		n,age,nat,sal,gr,exp=str.split()
		return cls(n,age,nat,sal,gr,exp)




	def salage(self, *arg):
		if(len(arg) == 1):
			self.__salary=arg[0]
		else:
			self.__salary=arg[0]
			saad.changeage(self,arg[1])



	def prin(self):
		print(self.name,self.__salary)
		self.printage()

if(__name__ == "__main__"):
	saad= Employee("saad",30,"pak",30000,"a","5 year")
	saad.prin()
	saad.salage([50000,40])
	saad.prin()


	ali=Employee.empstr("ali_ahmad 28 pakistan 35000 a 5_year")
	ali.prin()
