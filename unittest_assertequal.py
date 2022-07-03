import unittest
import fn_under_test

class unittest_assertequal(unittest.TestCase):

	# + scenario
	def test_assertequal_pos(self):  #method that tests the function 
		self.assertEqual(fn_under_test.getstring(),"Vinoth") #testing by calling the function and passing the predicted result

	# - scenario
	def test_assertequal_neg(self):  #method that tests the function 
		self.assertEqual(fn_under_test.getstring(),"vinoth") #testing by calling the function and passing the predicted result

        
if __name__=="__main__":
	unittest.main()