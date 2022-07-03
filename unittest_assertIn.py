import unittest
import fn_under_test

class unittest_assertIn(unittest.TestCase):

	# + scenario
	def test_assertIn_pos(self):  #method that tests the function 
		self.assertIn("Vino",fn_under_test.getstring(),"assertIn Failed string does not contains substring")  #testing by calling the function and passing the predicted result

	# - scenario
	def test_assertIn_neg(self):  #method that tests the function 
		self.assertIn("vino",fn_under_test.getstring(),"assertIn Failed string does not contains substring") 

        
if __name__=="__main__":
	unittest.main()