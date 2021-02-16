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

	def sort(self):
		start=self.head
		temp=start.next
		while(start.next != self.head):
			while(temp.next != self.head):
				if(start.data > temp.data):
					tdata=temp.data
					temp.data=self.head.data
					self.head.data=tdata
				temp=temp.next
			start=start.next

	def show(self):
		temp=self.head
		while(temp.next != self.head):
			print(temp.data)
			temp=temp.next
		print(temp.data)

cl=llist()
cl.add(1)
cl.add(45)
cl.add(32)
cl.add(112)
cl.add(87)
cl.show()
print()
cl.sort()
cl.show()
