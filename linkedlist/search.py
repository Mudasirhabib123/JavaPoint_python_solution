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

	def search(self,val):
		temp=self.head
		while(temp.next != self.head):
			if(temp.data == val):
				return 1
			temp=temp.next

		return 0
cl=llist()
cl.add(1)
cl.add(2)
cl.add(3)
cl.add(4)
a=cl.search(2)
if(a):
	print(f"value found")
else:
	print("value not found")
