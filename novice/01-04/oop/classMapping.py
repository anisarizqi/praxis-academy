class Mapping:
	def __init__(self, iterable):
		self.items_list = []
		self.__update(iterable)

	def update(self, iterable):
		for item in iterable:
			self.items_list.append(item)

	__update = update


class MappingSubclass(Mapping):
	"""docstring for MappingSubclass"""
	def update(self, key, values):
		for item in zip(keys, values):
			self.items_list.append(item)
		