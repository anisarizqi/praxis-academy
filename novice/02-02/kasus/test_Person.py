
import unittest

class Person(unittest.TestCase):

	def test_true(self):

		self.assertFalse('Hello, my name is ANISA'.islower())

if __name__=='__main__':
	unittest.main()