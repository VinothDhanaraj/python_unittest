import unittest
import fn_under_test

class unittest_assertTrue(unittest.TestCase):

	# + scenario
	def test_assertTrue_pos(self):  #method that tests the function 
		self.assertTrue(fn_under_test.simple_interest(100,.09,60)==100*.09*60) #testing by calling the function and passing the predicted result

	# - scenario
	def test_assertTrue_neg(self):  #method that tests the function 
		self.assertTrue(fn_under_test.simple_interest(100,.09,60)==100.01*.09*60) #testing by calling the function and passing the predicted result

        
if __name__=="__main__":
	unittest.main()