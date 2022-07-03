import unittest
import fn_under_test

class unittest_assertFalse(unittest.TestCase):

	# + scenario
	def test_assertFalse_pos(self):  #method that tests the function 
		self.assertFalse(fn_under_test.getstring()=="Voo") #testing by calling the function and passing the predicted result

	# - scenario
	def test_assertFalse_neg(self):  #method that tests the function 
		self.assertFalse(fn_under_test.getstring()=="Vinoth") #testing by calling the function and passing the predicted result

        
if __name__=="__main__":
	unittest.main()