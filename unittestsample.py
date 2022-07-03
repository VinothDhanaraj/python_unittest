import unittest
import sample_code

class sample_unittest_python(unittest.TestCase):

	def test_sampletest(self):
		self.assertTrue(1==1)


	def test_sample_code(self):  #method that tests the function 
		self.assertEqual(sample_code.prod(4,-2),-8) #testing by calling the function and passing the predicted result
        
if __name__=="__main__":
	unittest.main()