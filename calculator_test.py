import unittest

# This is the class we want to test. So, we need to import it
import Calculator as CalculatorClass

class Test(unittest.TestCase):
    calculator = CalculatorClass.Calculator() # instantiate the Calculator Class
    def test_0_add(self):
        result = self.calculator.add(4,8)
        self.assertEqual(result,12)
class Test1(unittest.TestCase):
    calculator = CalculatorClass.Calculator() # instantiate the Calculator Class
    def test_0_add(self):
        result1 = self.calculator.subtract(10,8)
        self.assertEqual(result1,2)
class Test2(unittest.TestCase):
    calculator = CalculatorClass.Calculator() # instantiate the Calculator Class
    def test_0_add(self):        
        result2 = self.calculator.multiply(2,8)
        self.assertEqual(result2,16)
class Test3(unittest.TestCase):
    calculator = CalculatorClass.Calculator() # instantiate the Calculator Class
    def test_0_add(self):        
        result3 = self.calculator.divide(8,4)
        self.assertEqual(result3,2)
        
if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()