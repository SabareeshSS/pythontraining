'''
Created on 01-Jun-2016

@author: BALASUBRAMANIAM
'''
from pip._vendor.distlib.compat import raw_input
for _ in (0, 1, 2, 3, 4, 5):
    print("Welcome")
    
while True:
    line = raw_input('> ')
   
    if line == 'done':
            break
    print(line)

import random
for i in range(10):
    x = random.random()
    print (x)

t=[5,6,8,9,2,1,1,100]
print(random.choice(t))