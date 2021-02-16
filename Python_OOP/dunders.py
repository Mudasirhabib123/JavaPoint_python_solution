class mobile:
	def __init__(self,brand,model,color,price):
		self.brand=brand
		self.model=model
		self.color=color
		self.price=price

	def __add__(n,o):
		return n.price + o.price


new=mobile("nokia",1112,"black",2000)
old=mobile("n0kia",1100,"white",1500)

print(new+old)


