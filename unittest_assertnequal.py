import unittest
import fn_under_test

class unittest_assertnequal(unittest.TestCase):

	# + scenario
	def test_assertnequal_pos(self):  #method that tests the function 
		self.assertNotEqual(fn_under_test.simple_interest(100,.09,60),99.99*.09*60) #testing by calling the function and passing the predicted result

	# - scenario
	def test_assertnequal_neg(self):  #method that tests the function 
		self.assertNotEqual(fn_under_test.simple_interest(100,.09,60),100*.09*60) #testing by calling the function and passing the predicted result

        
if __name__=="__main__":
	unittest.main()