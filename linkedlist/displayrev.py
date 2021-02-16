class node:
	def __init__(self,data):
		self.data=data
		self.next=None

class llist:
	def __init__(self):
		self.head=self.tail=node(None)
		self.tail.next=self.head
		self.head.next=self.tail
	def add(self,data):
		nnode=node(data)
		if(self.head == None):
			self.head=self.tail=nnode
		else:
			self.tail.next=nnode
			nnode.next=self.head
			self.tail=nnode
		self.tail.next=self.head

	def showrev(self):
		temp=self.head
		c=1
		while(temp.next!= self.head):
			c+=1
			temp=temp.next
		temp=self.head
		d=c
		for i in range(1,d):
			c=d-1
			while(c):
				temp=temp.next
				c-=1
			print(temp.data)



cl=llist()
cl.add(1)
cl.add(2)
cl.add(3)
cl.showrev()
