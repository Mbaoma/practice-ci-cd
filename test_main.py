import unittest 
#Standard library

from sum_num.main import sumTo, addTwo, addNum
#from folder.file import function

class TestSum(unittest.TestCase):
    def test_sumTo(self):
        self.assertEqual(sumTo([1, 2, 3]), 6, "Should be 6")
        
    def test_addTwo(self):
        self.assertEqual(addTwo(4), 8, "Should be 6")
    
    def test_addNum(self):
        self.assertTrue(addNum(10), 20)

if __name__ == '__main__':
    unittest.main()