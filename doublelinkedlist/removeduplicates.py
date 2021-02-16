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

	def remove(self):
		temp=self.head
		while(temp.next != None):
			c=temp.next
			while(c.next != None):
				if(c.data == temp.data):
					c.prev.next=c.next
					if(c.next != None):
						c.next.prev=c.prev
				c=c.next
			temp=temp.next
cl=dlist()
cl.add(1)
cl.add(2)
cl.add(3)
cl.add(3)
cl.add(4)
cl.add(5)
cl.show()
print()
cl.remove()
cl.show()
