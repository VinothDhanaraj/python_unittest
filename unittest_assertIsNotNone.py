import unittest
import object_under_test

class unittest_assertIsNotNone(unittest.TestCase):

	# + scenario
	def test_assertIsNotNone_pos(self):  #method that tests the function 
		self.assertIsNotNone(object_under_test.thirdValue,"assertIsNone Failed ,since object is None") 

	# - scenario
	def test_assertIsNotNone_neg(self):  #method that tests the function 
		self.assertIsNotNone(object_under_test.fourthValue,"assertIsNone Failed ,since object is None") 

        
if __name__=="__main__":
	unittest.main()