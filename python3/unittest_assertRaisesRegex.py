import unittest
import fn_under_test

class unittest_assertRaisesRegex(unittest.TestCase):

	# + scenario
	def test_assertRaisesRegex_pos(self):  #method that tests the function 
		args=[6,0]
		self.assertRaisesRegex(Exception,".*zero.*",fn_under_test.divide_by_zero,*args)

	# - scenario
	def test_assertRaisesRegex_neg(self):  #method that tests the function 
		args=[6,6]
		self.assertRaisesRegex(Exception,".*zero.*",fn_under_test.divide_by_zero,*args)

        
if __name__=="__main__":
	unittest.main()