'''
Created on 04-Nov-2016

@author: BALASUBRAMANIAM
'''
import os
import re
pathname="g:/local disk/python/NovBoschDay2Training"
os.chdir(pathname)
#data=open('sample.txt','r')
data=open('product.csv','r')
#print(data.read())
row=[]
for line in data:    
    row.append(re.findall('\w+',line))
data.close()
#print(row)

for r in row:
    if(len(r)>0):
        for col in r:
            if(col=='Wheel'):
                print(col)
                
print(row[2][1])