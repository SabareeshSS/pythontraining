'''
Created on 03-Nov-2016

@author: BALASUBRAMANIAM
'''
import statistics
print(statistics.mean([4,5,6]))
print(statistics.median([5,5,6,7]))
print(statistics.mode([1, 1, 2, 3, 3, 3, 3, 4]))
from fractions import Fraction as F
print(statistics.mean([F(3, 7), F(1, 21), F(5, 3), F(1, 3)]))
print(statistics.Fraction(13,21))

from decimal import Decimal as D
print(statistics.mean([D("0.5"), D("0.75"), D("0.625"), D("0.375")]))
