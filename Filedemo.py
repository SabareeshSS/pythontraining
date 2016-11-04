'''
Created on 04-Nov-2016

@author: BALASUBRAMANIAM
'''
import os
from datetime import date
print(os.getcwd())
os.chdir("g:/local disk/python")
print(os.getcwd())
#os.mkdir("g:\\local disk\\python\\NovBoschDay2Training")
pathname = '/Users/pilgrim/diveintopython3/examples/test.py'
print(os.path.split(pathname))
pathname="g:/local disk/python/NovBoschDay2Training"
file=open(pathname+"/machine.log",'a')
file.write("Started Logging.........")
file.write(date.today().strftime("%d/%m/%Y"))
info=input("Enter Tester Name")
file.write(info)
file.close()
os.chdir(pathname)
#os.remove("machine.log")
os.chdir("c:/")
print(os.listdir('.'))
print(os.getpid())

