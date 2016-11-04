'''
Created on 03-Jun-2016

@author: BALASUBRAMANIAM
'''
import unittest
from boschtraining.finance import addTax
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_numbers_3_4(self):
        self.assertEqual( addTax(46985,2), 47924.700000000004)
 
    
 
if __name__ == '__main__':
    unittest.main()
