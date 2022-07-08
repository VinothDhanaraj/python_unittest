import unittest
import fn_under_test
import object_under_test

class all_unittest(unittest.TestCase):

	def setUp(self):
		print('\nTEST SETUP TEST SETUP TEST SETUP TEST SETUP TEST SETUP TEST SETUP TEST SETUP')

	def tearDown(self):
		print('\nTEST TEARDOWN TEST TEARDOWN TEST TEARDOWN TEST TEARDOWN TEST TEARDOWN TEST TEARDOWN')

	# + scenario
	def test_assertequal_pos(self):  #method that tests the function 
		self.assertEqual(fn_under_test.getstring(),"Vinoth") #testing by calling the function and passing the predicted result

	# - scenario
	def test_assertequal_neg(self):  #method that tests the function 
		self.assertEqual(fn_under_test.getstring(),"vinoth") #testing by calling the function and passing the predicted result

	# + scenario
	def test_assertnequal_pos(self):  #method that tests the function 
		self.assertNotEqual(fn_under_test.simple_interest(100,.09,60),99.99*.09*60) #testing by calling the function and passing the predicted result

	# - scenario
	def test_assertnequal_neg(self):  #method that tests the function 
		self.assertNotEqual(fn_under_test.simple_interest(100,.09,60),100*.09*60) #testing by calling the function and passing the predicted result

	# + scenario
	def test_assertTrue_pos(self):  #method that tests the function 
		self.assertTrue(fn_under_test.simple_interest(100,.09,60)==100*.09*60) #testing by calling the function and passing the predicted result

	# - scenario
	def test_assertTrue_neg(self):  #method that tests the function 
		self.assertTrue(fn_under_test.simple_interest(100,.09,60)==100.01*.09*60) #testing by calling the function and passing the predicted result

	# + scenario
	def test_assertFalse_pos(self):  #method that tests the function 
		self.assertFalse(fn_under_test.getstring()=="Voo") #testing by calling the function and passing the predicted result

	# - scenario
	def test_assertFalse_neg(self):  #method that tests the function 
		self.assertFalse(fn_under_test.getstring()=="Vinoth") #testing by calling the function and passing the predicted result
		


	# + scenario
	def test_assertIn_pos(self):  #method that tests the function 
		self.assertIn("Vino",fn_under_test.getstring(),"assertIn Failed string does not contains substring")  #testing by calling the function and passing the predicted result

	# - scenario
	def test_assertIn_neg(self):  #method that tests the function 
		self.assertIn("vino",fn_under_test.getstring(),"assertIn Failed string does not contains substring") 


		
	# + scenario
	def test_assertNotIn_pos(self):  #method that tests the function 
		self.assertNotIn("Xino",fn_under_test.getstring(),"assertIn Failed string contains substring") 
		
	# - scenario
	def test_assertNotIn_neg(self):  #method that tests the function 
		self.assertNotIn("Vino",fn_under_test.getstring(),"assertIn Failed string contains substring")

	# + scenario
	def test_assertIs_pos(self):  #method that tests the function 

		self.assertIs(object_under_test.firstValue,object_under_test.secondValue,"assertIs Failed ,since object is different")

	# - scenario
	def test_assertIs_neg(self):  #method that tests the function 
		self.assertIs(object_under_test.firstValue,object_under_test.thirdValue,"assertIs Failed ,since object is different") 


	# + scenario
	def test_assertIsNot_pos(self):  #method that tests the function 
		self.assertIsNot(object_under_test.firstValue,object_under_test.thirdValue,"assertIsNot Failed ,since object is same") 

	# - scenario
	def test_assertIsNot_neg(self):  #method that tests the function 
		self.assertIsNot(object_under_test.firstValue,object_under_test.secondValue,"assertIsNot Failed ,since object is same") 
		

	# + scenario
	def test_assertIsNone_pos(self):  #method that tests the function 
		self.assertIsNone(object_under_test.fourthValue,"assertIsNone Failed ,since object is not None") 

	# - scenario
	def test_assertIsNone_neg(self):  #method that tests the function 
		self.assertIsNone(object_under_test.thirdValue,"assertIsNone Failed ,since object is not None") 


	# + scenario
	def test_assertIsNotNone_pos(self):  #method that tests the function 
		self.assertIsNotNone(object_under_test.thirdValue,"assertIsNone Failed ,since object is None") 

	# - scenario
	def test_assertIsNotNone_neg(self):  #method that tests the function 
		self.assertIsNotNone(object_under_test.fourthValue,"assertIsNone Failed ,since object is None") 


	# + scenario
	def test_assertIsInstance_pos(self):  #method that tests the function 
		self.assertIsInstance(object_under_test.secondValue,object_under_test.object_under_test,"assertIsInstance Failed ,since object is not part the class")

	# - scenario
	def test_assertIsInstance_neg(self):  #method that tests the function 
		self.assertIsInstance(object_under_test.secondValue,object_under_test.object_under_test_1,"assertIsInstance Failed ,since object is not part the class")


	# + scenario
	def test_assertNotIsInstance_pos(self):  #method that tests the function 
		self.assertNotIsInstance(object_under_test.secondValue,object_under_test.object_under_test_1,"assertIsInstance Failed ,since object is part the class")

	# - scenario
	def test_assertNotIsInstance_neg(self):  #method that tests the function 
		self.assertNotIsInstance(object_under_test.secondValue,object_under_test.object_under_test,"assertIsInstance Failed ,since object is part the class")
        
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

