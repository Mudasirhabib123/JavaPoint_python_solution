class node:
	def __init__(self,data):
		self.data=data
		self.left=self.right=None

class bintree:
	def __init__(self):
		self.root=self.head=self.tail=None

	def bttodll(self,node):
		if(node == None):
			return
		self.bttodll(node.left)
		if(self.head == None):
			self.head=self.tail=node
		else:
			self.tail.right=node
			node.left=self.tail
			self.tail=node

		self.bttodll(node.right)

	def show(self):
		temp=self.head
		while(temp != None):
			print(temp.data)
			temp=temp.right
cl=bintree()

cl.root=node(1)
cl.root.left=node(2)
cl.root.right=node(3)
cl.root.left.left=node(4)
cl.root.left.right=node(5)
cl.root.right.left=node(6)
cl.root.right.right=node(7)
cl.bttodll(cl.root)
cl.show()
