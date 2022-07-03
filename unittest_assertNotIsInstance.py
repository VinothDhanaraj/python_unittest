import unittest
import object_under_test

class unittest_assertNotIsInstance(unittest.TestCase):

	# + scenario
	def test_assertNotIsInstance_pos(self):  #method that tests the function 
		self.assertNotIsInstance(object_under_test.secondValue,object_under_test.object_under_test_1,"assertIsInstance Failed ,since object is part the class")

	# - scenario
	def test_assertNotIsInstance_neg(self):  #method that tests the function 
		self.assertNotIsInstance(object_under_test.secondValue,object_under_test.object_under_test,"assertIsInstance Failed ,since object is part the class")

        
if __name__=="__main__":
	unittest.main()