class node:
	def __init__(self,data):
		self.data=data
		self.next=self.prev=None

class dlist:
	def __init__(self):
		self.head=self.tail=node(None)
		self.count=0

	def add(self,data):
		nnode=node(data)
		self.count+=1
		if(self.head == None):
			self.head=self.tail=nnode
			self.head.next=self.tail.next=None
		else:
			self.tail.next=nnode
			nnode.tail=self.tail
			self.tail=nnode
			self.tail.next=None

	def show(self):
		temp=self.head
		while(temp != None):
			print(temp.data)
			temp=temp.next

	def delmid(self):
		if(self.count %2):
			mid=(self.count)//2
		else:
			mid=(self.count+1)//2
		temp=self.head


		for i in range(1,mid):
			temp=temp.next

		if(temp==self.head):
			self.head=self.head.next
		elif(temp== self.tail):
			self.tail=self.tail.prev
		else:
			temp.next.prev=temp.prev
			temp.prev.next=temp.next




cl=dlist()
cl.add(1)
cl.add(2)
cl.add(3)
cl.add(4)
cl.add(5)
cl.show()
cl.delmid()
print()
cl.show()
