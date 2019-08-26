
def person():
	def __init__(self, name, age):
		self.name=name
		self.age=age

person = [{name:'peter', age:16},{name:'mark', age:18},
{name:'john', age:27},{name:'jane', age:14},{name:'tony', age:24},
]

fullAge = filter(lambda x: person.age >= 18)
print(list(fullAge))