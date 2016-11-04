'''
Created on 03-Nov-2016

@author: BALASUBRAMANIAM
'''
from pip._vendor.distlib.compat import raw_input
name = raw_input('What...is your name?\n')
print(name)
length=len(name)
if(length>25):
    print("Name exceeds 25 chars")
elif((length>10) and (length<25)):
    print("Name Length lies between 10 to 25")
else:
    print(name)