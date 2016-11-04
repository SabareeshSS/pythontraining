'''
Created on 03-Nov-2016

@author: BALASUBRAMANIAM
'''
data=(4,'keeranatham',True)
#print(data)
#data.append(4359)
nestedTuple=(('Ashok',567569756),('Aruna',356995345
                                  ),('Karthik',46704765467))
for tuple in nestedTuple:
    for data in tuple:
        print(data,"\t", end='')
    print()
    
hrData=list(nestedTuple)
print(hrData)