'''
Created on 04-Nov-2016

@author: BALASUBRAMANIAM
'''
import sys
#sys.path.insert(0, 'g:/local disk/python/NovBoschDay2Training/pythonlib')
sys.path.append('g:/local disk/python/NovBoschDay2Training/pythonlib')
#from test import PrintNames
#PrintNames()

from SumIt import sumList
from SumIt import SortNames
data=[6,7,8,3,4]
print(sumList(data))
from boschtraining.CurrencyConversion import USDTOINR
print(USDTOINR(1000))

names=["Jaya","Karuna","Bala","David"]
SortedData = SortNames(names)
for name in SortedData:
    print(name)
