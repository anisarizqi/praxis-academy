class Car:
	"""docstring for ClassName"""
	def __init__(self, wheels=4):
		self.wheels = wheels
			

class Gasoline(Car):
	"""docstring for ClassName"""
	def __init__(self, engine='Gasoline', tank_cap=20):
		Car.__init__(self)
		self.engine = engine
		self.tank_cap = tank_cap
		self.tank = 0

	def refuel(self):
		self.tank = self.tank_cap

class Electric(Car):
	"""docstring for Electric"""
	def __init__(self, engine='Electric', kwH_cap=60):
		Car.__init__(self)
		self.engine = engine
		self.kwH_cap = kwH_cap
		self.kwH = 0

	def recharge(self):
		self.kwH = self.kwH_cap

class Hybrid(Gasoline, Electric):
	"""docstring for Hybrid"""
	def __init__(self, engine='Hybrid', tank_cap=11, kwH_cap=5):
		Gasoline.__init__(self, engine, tank_cap)
		Electric.__init__(self, engine, kwH_cap)

prius = Hybrid()
print(prius.tank)
print(prius.kwH)

prius.recharge()
print(prius.kwH)
		
		
		
		
		