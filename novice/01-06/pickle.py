import pickle

class Animal:
	def __init__(self, number_of_paws, color):
		self.number_of_paws = number_of_paws
		self.color = color

class Sheep(Animal):
	"""docstring for Sheep"""
	def __init__(self, color):
		Animal.__init__(self, 4, color)
		
mary = Sheep("white")
print (str.format("My s"))