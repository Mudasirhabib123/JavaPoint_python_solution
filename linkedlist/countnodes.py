class node:
	def __init__(self,data):
		self.data =data
		self.next=None

class llist:
	def __init__(self):
		self.head=self.tail=node(None)
		self.head.next=self.tail
		self.tail.next=self.head

	def add(self,data):
		nnode=node(data)
		if(self.head == None):
			self.head=self.tail=node(None)
		else:
			self.tail.next=nnode
			nnode.next=self.head
			self.tail=nnode
		self.tail.next=self.head

	def count(self):
		temp=self.head
		c=0
		while(temp.next!= self.head):
			c +=1
			temp=temp.next
		return c

cl=llist()
cl.add(1)
cl.add(2)
cl.add(3)
print(cl.count())
