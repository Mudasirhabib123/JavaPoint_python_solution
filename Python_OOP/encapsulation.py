class employee:
	def __init__(self,n,s,a):
		self.name=n
		self._salary=s
		self.__age=a
	def setage(self,ag):
		self.__age=ag

	def prin(self):
		print(self.name,self._salary,self.__age)

ali=employee("ali",15000,30)
ali.prin()
ali.setage(40)
ali._salary=25000
ali.prin()
