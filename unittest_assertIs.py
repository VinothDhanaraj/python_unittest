import unittest
import object_under_test

class unittest_assertIs(unittest.TestCase):

	# + scenario
	def test_assertIs_pos(self):  #method that tests the function 

		self.assertIs(object_under_test.firstValue,object_under_test.secondValue,"assertIs Failed ,since object is different")

	# - scenario
	def test_assertIs_neg(self):  #method that tests the function 
		self.assertIs(object_under_test.firstValue,object_under_test.thirdValue,"assertIs Failed ,since object is different") 

        
if __name__=="__main__":
	unittest.main()