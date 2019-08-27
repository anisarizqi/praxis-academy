

import unittest

def add(a, b):
	return a + b

class test(unittest.TestCase):
	"""docstring for test"""
	def test(self):
		self.assertEqual (add(2, 4), 6)

if __name__ == '__main__':
	unittest.main()