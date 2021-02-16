class Radio:
	def __init__(self):
		print("only audio")

class Camera:
	def __init__(self):
		print("only pictures")

class Mobile(Radio,Camera):
	super().__init__()
	print("it contains both")

mob=Mobile()

