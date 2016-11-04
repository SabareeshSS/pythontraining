'''
Created on 03-Nov-2016

@author: BALASUBRAMANIAM
'''
'''
telephoneDir={9952032862:'Parameswari',805605010299:'Vignesh'}
#print(telephoneDir.keys())
#print(telephoneDir.values())
for(k,v) in telephoneDir.items():
    print(k,"\t",v)

#Retrieve value from key
print(telephoneDir.get(9952032862))
'''
employeeDb={23456:{'Name':'Ashok','Address':'Coimbatore'},
            456789:{'Name':'Seshayee','Address':'Chennai'},
            567857:{'Name':'Shiva','Address':'Bangalore'}          
                        
            }
#print(employeeDb.get(456789))
skey=employeeDb.get(456789)
for data in skey:
    print(skey[data],"\t",end='')

    