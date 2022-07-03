import unittest
import fn_under_test

class unittest_assertNotIn(unittest.TestCase):

	# + scenario
	def test_assertNotIn_pos(self):  #method that tests the function 
		self.assertNotIn("Xino",fn_under_test.getstring(),"assertIn Failed string contains substring") 
		
	# - scenario
	def test_assertNotIn_neg(self):  #method that tests the function 
		self.assertNotIn("Vino",fn_under_test.getstring(),"assertIn Failed string contains substring") 

        
if __name__=="__main__":
	unittest.main()