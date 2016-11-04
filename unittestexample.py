'''
Created on 04-Nov-2016

@author: BALASUBRAMANIAM
'''
import unittest
import sys
sys.path.append('g:/local disk/python/NovBoschDay2Training/pythonlib')
from SumIt import sumList
from SumIt import SortNames
class TestSumIt(unittest.TestCase):
    def setUp(self):
        pass
 
    def test_sumList(self):
        data=[6,7,1,2]
        self.assertEqual(sumList(data),16)
    def test_SortName(self):
        data=["Ravi","Anu"]
        self.assertListEqual(SortNames(data),data)
        
if __name__ == '__main__':
    unittest.main()
        