'''
Created on 01-Jun-2016

@author: BALASUBRAMANIAM
'''
import sys
import gc



print('Welcome to training')
print(type('a'))
data='qwertyt'
print( "Data%s\tSize=%d" %(data,sys.getsizeof(data)))
age=45
print("type of the Age")
print(type(age))
print(type(176))
print(type('Who am I'))
print(type(True))
print(type(12.5))
print(type('Bala'))
print(type(210624583337114373395836055367340864637790190801098222508621955072))
print("Hard Times"[5])

#Type conversion
print (type(int("45")))

print (type(str(9876)))
x="Test"
#size of
print("Size=%d" %(sys.getsizeof(x)))
x=None
gc.collect()
print("Size=%d" %(sys.getsizeof(x)))

x=67
print("Size=%d" %(sys.getsizeof(x)))


#print("Size=%d" %(sys.getsizeof(x)))
#Object reference -- variable and object reference interchangeable
x = "blue"
y = "green"
z = x
print(x,y,z)
z=y
print(x,y,z)

#Multi line comments
'''
Collection Data Types
Tuples
'''
tupledata =("Denmark", "Finland", "Norway", "Sweden")
print (tupledata)
#List
listdata=["Denmark", "Finland", "Norway", "Sweden"]
print (listdata)

print(len([3, 5, 1, 2, "pause", 5]))
listdata.append("Montreal")
print(listdata)
print("Size=%d" %(sys.getsizeof(listdata)))
del listdata
#print(listdata)

#print("Size=%d" %(sys.getsizeof(listdata)))


