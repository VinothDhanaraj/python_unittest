import unittest
import fn_under_test

class unittest_assertLogs(unittest.TestCase):

	# + scenario
	def test_assertLogs_pos(self):  #method that tests the function 
		vin_logs=self.assertLogs()
		self.assertIn('Vinoth warning msg', vin_logs)
		
	# - scenario
#	def test_assertLogs_neg(self):  #method that tests the function 
#		self.assertLogs("Vino",fn_under_test.getstring(),"assertIn Failed string contains substring") 
		
        
if __name__=="__main__":
	unittest.main()