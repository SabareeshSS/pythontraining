'''
Created on 01-Jun-2016

@author: BALASUBRAMANIAM
'''
import os
import glob
print(os.getcwd())
os.chdir('c:/users')
print(os.getcwd())
pathname = '/Users/pilgrim/diveintopython3/examples/humansize.py'
print(os.path.split(pathname))
(dirname, filename) = os.path.split(pathname)
print(dirname)
print(filename)
(shortname, extension) = os.path.splitext(filename)
print(shortname)
print (extension)

os.chdir('c:/users')
print(glob.glob('/*.*'))

#os.makedirs('C:\\python\\walnut\\waffles')