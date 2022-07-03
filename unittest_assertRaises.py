import unittest
import fn_under_test

class unittest_assertRaises(unittest.TestCase):

	# + scenario
	def test_assertRaises_pos(self):  #method that tests the function 
		args=[6,0]
		self.assertRaises(ZeroDivisionError,fn_under_test.divide_by_zero,*args)

	# - scenario
	def test_assertRaises_neg(self):  #method that tests the function 
		args=[6,6]
		self.assertRaises(ZeroDivisionError,fn_under_test.divide_by_zero,*args)

        
if __name__=="__main__":
	unittest.main()