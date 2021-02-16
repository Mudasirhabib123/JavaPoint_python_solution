class node:
	def __init__():
		self.data=data
		self.next=None

class llist:
	def __init__():
		self.head=self.tail=node(None)
		self.head.next=self.tail
		self.tail.next=self.head
		self.count=0

	def add(self,data):
		nnode=node(data)
		if(self.head==None):
			self.head=self.tail=nnode
		else:
			self.tail.next=nnode
			nnode.next=self.head
			self.tail=nnode
		self.tail.next=self.head
		self.count+=1

	def delmid(self):
		if(count%2):
			mid=(count+1)/2
		else:
			mid=count/2

		temp=self.head
		for i in range(mid):
			temp=temp.next

		c=temp.next
		temp.next=c.next

	def show(self):
		temp=self.head
		while(temp.next != self.head):
			print(temp.data)
			tepm=temp.next
		print(temp.data)
cl=llist()
cl.add(1)
cl.add(2)
cl.add(3)
cl.add(5)
cl.add(4)
cl.add(6)
cl.add(7)
cl.show()
#cl.delmid()
print()
cl.show()
