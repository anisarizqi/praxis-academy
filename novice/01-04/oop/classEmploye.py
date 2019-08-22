class Employee:
	def __init__(self, name):
		self.name = name
		print('my name', self.name)

john = Employee()

john.name = 'John Doe'
john.dept = 'Computer Lab'
john.salary = 1000