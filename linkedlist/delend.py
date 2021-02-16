class node:
	def __init__(self,data):
		self.data=data
		self.next=None

class llist:
	def __init__(self):
		self.head=self.tail=node(None)
		self.head.next=self.tail
		self.tail.next=self.head

	def add(self,data):
		nnode=node(data)
		if(self.head == None):
			self.head=self.tail=nnode
		else:
			self.tail.next=nnode
			nnode.next=self.head
			self.tail=nnode
		self.tail.next=self.head

	def show(self):
		temp=self.head
		while(temp.next != self.head):
			print(temp.data)
			temp=temp.next
		print(temp.data)

	def delend(self):
		temp=self.head
		while(temp.next != self.tail):
			temp=temp.next
		self.tail=temp
		self.tail.next=self.head

cl=llist()
cl.add(1)
cl.add(2)
cl.add(3)
cl.show()
print()
cl.delend()
cl.show()

