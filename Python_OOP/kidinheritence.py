class kid:
	def __init__(self,n,age,h):
		self.name=n
		self.age=age
		self.hobby=h

class student(kid):
	def __init__(self,n,age,h,rno,mark):
		super(). __init__(n,age,h)
		self.rolnmb=rno
		self.marks=mark

ali=student("Ali",12,"cricket",25,50)
print(ali.name,ali.rolnmb)
