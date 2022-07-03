import unittest
import object_under_test

class unittest_assertIsNot(unittest.TestCase):

	# + scenario
	def test_assertIsNot_pos(self):  #method that tests the function 
		self.assertIsNot(object_under_test.firstValue,object_under_test.thirdValue,"assertIsNot Failed ,since object is same") 

	# - scenario
	def test_assertIsNot_neg(self):  #method that tests the function 
		self.assertIsNot(object_under_test.firstValue,object_under_test.secondValue,"assertIsNot Failed ,since object is same") 

        
if __name__=="__main__":
	unittest.main()