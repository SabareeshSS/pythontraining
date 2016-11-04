'''
Created on 03-Nov-2016

@author: BALASUBRAMANIAM
'''
from enum import Enum, unique
@unique
class BugLevel(Enum):
    Error = 1
    Warning = 2
    Info = 3

print(BugLevel(2))
print(type(BugLevel(1)))

'''
class IceCream(Enum):
    vanilla = 7
    chocolate = 4
    cookies = 9
    mint = 3

for shake in IceCream:
    print(shake)
'''