class node:
	def __init__(self,data):
		self.data=data
		self.next=None

class llist:
	def __init__(self):
		self.head=self.tail=node(None)
		self.head.next=self.tail
		self.tail.next=self.head
		self.count=0

	def add(self,data):
		nnode=node(data)
		if(self.head == None):
			self.head=self.tail=nnode
		else:
			self.tail.next=nnode
			nnode.next=self.head
			self.tail=nnode
		self.tail.next=self.head
		self.count+=1

	def addmid(self,data):
		nnode=node(data)
		if(self.count %2):
			mid=(self.count+1)//2
		else:
			mid=self.count//2
		temp=self.head
		for i in range(1,mid):
			temp=temp.next
		temp.next=nnode
		nnode.next=temp.next
		self.count+=1

	def show(self):
		temp=self.head
		while(temp.next != self.head):
			print(temp.data)
			temp=temp.next
		print(temp.data)

cl=llist()
cl.add(1)
cl.add(2)
cl.add(3)
cl.add(5)
cl.addmid(4)
cl.show()
print()
cl.addmid(5)
