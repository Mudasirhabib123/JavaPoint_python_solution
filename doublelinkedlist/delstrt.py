class node:
	def __init__(self,data):
		self.data=data
		self.next=self.prev=None

class dlist:
	def __init__(self):
		self.head=self.tail=node(None)

	def add(self,data):
		nnode=node(data)
		if(self.head == None):
			self.head=self.tail=nnode
			self.head.next=self.tail.next=None
		else:
			self.tail.next=nnode
			nnode.prev=self.tail
			self.tail=nnode
			self.tail.next=None

	def show(self):
		temp=self.head
		while(temp != None):
			print(temp.data)
			temp=temp.next

	def delstrt(self):
		if(self.head == None):
			return 
		elif(self.head != self.tail):
			self.head=self.head.next
			self.head.prev=None
		else:
			self.head=self.tail=None











cl=dlist()
cl.add(1)
cl.add(2)
cl.add(3)
cl.show()
print()
cl.delstrt()
cl.show()
