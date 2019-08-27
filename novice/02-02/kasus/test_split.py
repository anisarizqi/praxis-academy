
import unittest

class TestSum(unittest.TestCase):
	def tes_split(self):
		s = 'hello anisa'
		self.assertEqual(s.split(), ['hello', 'anisa'])
		with self.assertRaises(TypeError):
			s.split(1)

if __name__=='__main__':
	unittest.main()