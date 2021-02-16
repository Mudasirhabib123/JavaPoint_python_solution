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

	def rotate(self,nmb):
		if(self.head == None):
			return
		else:
			if(self.head == self.tail):
				return
			else:
				for i in range(nmb):
					tdata=self.head.data
					temp=self.head
					print()
					print(tdata)
					n=temp.next
					while(n.next != None):
						temp.data=temp.next.data
						temp=temp.next
						n=temp.next
					temp=temp.prev
					temp.data=tdata



cl=dlist()
cl.add(1)
cl.add(2)
cl.add(3)
cl.show()
cl.rotate(1)
print()
cl.show()
