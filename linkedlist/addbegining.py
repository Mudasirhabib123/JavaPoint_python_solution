class node:
	def __init__(self,data):
		self.data=data
		self.next=None

class llist:
	def __init__(self):
		self.head=self.tail=node(None)
		self.head.next=self.tail
		self.tail.next=self.head

	def addbeg(self,data):
		nnode=node(data)
		if(self.head == None):
			self.head=self.tail=nnode
		else:
			nnode.next=self.head
			self.head=nnode
		self.tail.next=self.head
	def show(self):
		temp=self.head
		while(temp.next!= self.head):
			print(temp.data)
			temp=temp.next
#		print(temp.data)
cl=llist()
cl.addbeg(1)
cl.addbeg(2)
cl.addbeg(3)
cl.show()
