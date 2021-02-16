from abc import ABC,abstractmethod

class shape(ABC):
	@abstractmethod
	def printarea(self):
		return 0

	@abstractmethod
	def patribute(self):
		pass


class square(shape):
	def __init__(self,s):
		self.size=s

	def printarea(self):
		print(self.size * self.size)


	def patribute(self):
		print(self.size)

class rectangle(shape):
	def __init__(self,l,w):
		self.length=l
		self.width=w
	def printarea(self):
		print(self.length * self.width)


	def patribute(self):
		print(self.length,"\t",self.width)


a=square(5)

a.printarea()

b=rectangle(7,5)

b.printarea()
a.patribute()

b.patribute()
