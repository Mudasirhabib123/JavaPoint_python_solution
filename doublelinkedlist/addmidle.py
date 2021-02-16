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
			nnode.prev=self.tail
			self.tail=nnode
			self.tail.next=None
	def addmid(self,data):
		if(self.head == None):
			return
		elif(self.head == self.tail):
			nnode=node(data)
			self.tail.next=nnode
			nnode.prev=self.tail
			self.tail=nnode
		else:
			if(self.count %2):
				mid=self.count//2
			else:
				mid=(slf.count)//2
			temp=self.head
			for i in range(mid):
				temp=temp.next
			nnode=node(data)
			nnode.prev=temp
			temp.next=nnode
			nnode.next=temp.next
			nnode.prev=temp

		self.tail.next=None
	def show(self):
		temp=self.head
		while(temp != None):
			print(temp.data)
			temp=temp.next

cl=dlist()
cl.add(1)
cl.add(2)
cl.add(3)
cl.show()
cl.addmid(4)
cl.addmid(5)
print()
cl.show()
