class node:
	def __init__(self,data):
		self.data=data
		self.next=self.prev=None

class dlist:
	def __init__(self):
		self.head=self.tail=node(None)

	def addend(self,data):
		nnode=node(data)
		if(self.head == None):
			self.head=self.tail=nnode
			self.head.next=self.tail.next=None
		else:
			self.tail.next=nnode
			nnode.next=None
			self.tail=nnode
			self.tail.next=None

	def show(self):
		temp=self.head
		while(temp != None):
			print(temp.data)
			temp=temp.next

cl=dlist()
cl.addend(1)
cl.addend(2)
cl.addend(3)
cl.show()
