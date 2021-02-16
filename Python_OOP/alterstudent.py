class student:
	def __init__(self,name,rno,marks):
		self.name = name
		self.rno = rno
		self.marks = marks

	@classmethod
	def altercons(cls,str):
		name,rno,marks=str.split()
		rno=int(rno)
		marks=int(marks)
		return cls(name,rno,marks)

ali=student("ali",22,50)
saad=student("saad",23,50)


print(saad.name,saad.rno,saad.marks)
print()
print(ali.name,ali.rno,ali.marks)

adnan=student.altercons("adnan 25 49")
print(adnan.name,adnan.rno,adnan.marks)
