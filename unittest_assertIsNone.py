import unittest
import object_under_test

class unittest_assertIsNone(unittest.TestCase):

	# + scenario
	def test_assertIsNone_pos(self):  #method that tests the function 
		self.assertIsNone(object_under_test.fourthValue,"assertIsNone Failed ,since object is not None") 

	# - scenario
	def test_assertIsNone_neg(self):  #method that tests the function 
		self.assertIsNone(object_under_test.thirdValue,"assertIsNone Failed ,since object is not None") 

        
if __name__=="__main__":
	unittest.main()