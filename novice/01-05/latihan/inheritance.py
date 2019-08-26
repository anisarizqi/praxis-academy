class Animal:
	def __init__(self, name):
		self.name = name

	def speak(self):
		raise NotImplementedError("Subclass must implemented abstract method")


class Dog(Animal):
	def speak(self):
		return self.name+' says Woof!'

class Cat(Animal):
	def speak(self):
		return self.name+' says Meoww!'

fido = Dog('Fido')
isis = Cat('Isis')

print(fido.speak())
print(isis.speak())