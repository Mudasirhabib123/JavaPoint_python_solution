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
			nnode.next=None
			self.tail=nnode
			self.tail.next=None

	def show(self):
		temp=self.head
		while(temp != None):
			print(temp.data)
			temp=temp.next

	def count(self):
		c=0
		temp=self.head
		while(temp.next != None):
			c+=1
			temp=temp.next
		print(f"total nodes in linked list are {c}")
cl=dlist()
cl.add(1)
cl.add(2)
cl.add(3)
cl.show()
cl.count()
