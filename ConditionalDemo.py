'''
Created on 01-Jun-2016

@author: BALASUBRAMANIAM
'''

if __name__ == '__main__':
    print ('This program is being run by itself')
else:
 print ('I am being imported from another module')
    
    
    
    
    
s = input("enter an integer: ")
try:
    i = int(s)
    print("valid integer entered:", i)
except ValueError as err:
    print(err)