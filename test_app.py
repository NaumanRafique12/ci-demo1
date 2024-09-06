import unittest
from app import add, sub

class TestMathFunctions(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(2,2),4)
        self.assertEqual(add(2,20),22)
        
        
    def test_sub(self):
        self.assertEqual(sub(2,2),0)
        self.assertEqual(sub(2,20),-18)
        
if __name__ == '__main__':
    unittest.main()
    
        