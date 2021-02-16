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
		if(self.head== None):
			self.head=self.tail=nnode
		else:
			self.tail.next=nnode
			nnode.next=self.head
			self.tail=nnode
		self.tail.next=self.head

	def remove(self):
		temp=self.head
		while(temp.next != self.head):
			start=temp.next
			while(start.next != self.head):
				if(temp.data == start.data):
					temp=temp.next
			start=start.next
		temp=temp.next
	def show(self):
		temp=self.head
		while(temp.next != self.head):
			print(temp.data)
			temp=temp.next
		print(temp.data)



cl=llist()
cl.add(3)
cl.add(2)
cl.add(2)
cl.add(3)
cl.add(2)

cl.show()
print()
cl.remove()
cl.show()
