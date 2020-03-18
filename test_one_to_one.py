import unittest
from one_to_one import one_to_one

class test_one_to_one(unittest.TestCase):
	def test_isomorphic(self):
		# Test one-to-one mapping when both inputs are strings of length n
		self.assertEqual(one_to_one('foo','bar'), False)
		self.assertEqual(one_to_one('hello','jpppr'), False)
		self.assertEqual(one_to_one('helLo','jePpr'), True)
		self.assertEqual(one_to_one('title','paper'), True)
		self.assertEqual(one_to_one('123', '321'), True)

	def test_values(self):
		# Make sure value errors are raised when necessary
		self.assertRaises(ValueError, one_to_one, 'foo','b')
		self.assertRaises(ValueError, one_to_one, 'f','bar')
		self.assertRaises(ValueError, one_to_one, '333', '   ')
		self.assertRaises(ValueError, one_to_one, '321 321','123 123')
		self.assertRaises(ValueError, one_to_one, '', '')
		


	def test_types(self):
		# Make sure type errors are raised when necessary
		self.assertRaises(TypeError, one_to_one, 123, 321)
		self.assertRaises(TypeError, one_to_one, '123', 321)
		self.assertRaises(TypeError, one_to_one, 123, '321')
		self.assertRaises(TypeError, one_to_one, True, '321')
		self.assertRaises(TypeError, one_to_one, '321')
		
	
