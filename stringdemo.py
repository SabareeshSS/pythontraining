'''
Created on 03-Nov-2016

@author: BALASUBRAMANIAM
'''
'''
#rawstring
print(r'd:\table')
#multiline string
statement=('python is scalable,'
               'object oriented and compact')
print(statement)
code="<a href='http://www.google.com'>Click Here</a>\n"
print(code[9:30])
print(code[-6:])
print(statement.capitalize())
print(code*4)#replicate the string
firstName="Robert Bosch"
print(firstName.casefold())
'''
firstName='Robert Bosch'
print(firstName.center(len(firstName)+15,'*'))
print(firstName.upper())
firstName='ROBERT BOSCH'
print(firstName.lower())
firstName='Robert BOSCH'
print(firstName.casefold())
data="ArunKumar-Coimbatore-1342454-Bosch"
print(data.partition("-"))
print(data.split(sep="-"))

arrayInfo=data.split(sep="-")
print(arrayInfo[2])
