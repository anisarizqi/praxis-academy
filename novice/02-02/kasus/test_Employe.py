import unittest

class Employee:
	def __init__(self, name, lab, age):
		self.name = name
		self.lab = lab
		self.age = age

john = Employee('john', 'computer lab', 40)


class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(john.name, 'john')

if __name__=='__main__':
	unittest.main()