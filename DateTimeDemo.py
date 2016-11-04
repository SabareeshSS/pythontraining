'''
Created on 02-Jun-2016

@author: BALASUBRAMANIAM
'''
from datetime import date

print(date.today().strftime("%d/%m/%Y"))

fmdate=date(2015,5,1)
print(fmdate)
print(date.today()-fmdate)
