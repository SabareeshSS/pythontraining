'''
Created on 02-Jun-2016

@author: BALASUBRAMANIAM
'''
import re
result=re.match(r'tech','technology we learn tech')
print (result.group())


phonePattern = re.compile(r'^(\d{4})-(\d{3})-(\d{3})$')
print(phonePattern.search('8124-456-343').groups())



phonePattern = re.compile(r'^(\d{3})\.(\d{3})\.(\d{4})\D*(\d*)$')
print(phonePattern.search('800.555.1212 x1234').groups())

#email matching
#difference beween . and \.
result=re.findall(r'\w+@([a-z]+\.\w+)','abctest@gmail1234.com, xyz@test.in')
print (result)

result=re.match(r'AV', 'AV audio AV audio')
print (result)
result=re.findall(r'AV', 'AV audio AV audio')
print(result)

result=re.split(r'i','Analytics Vidhya')
print (result)

result=re.split(r'i','Analytics Vidhya',maxsplit=1)
print (result)

result=re.sub(r'India','the World','AV is largest Analytics community of India')
print (result)
result=re.findall(r'\w*','AV is largest Analytics community of India')
print (result)
result=re.findall(r'\w+','AV is largest Analytics community of India')
print (result)
result=re.findall(r'\w\w','AV is largest Analytics community of India')
print (result)
result=re.findall(r'\b\w.','AV is largest Analytics community of India')
print (result)

result = re.match('Hello How are you',"Hello How are you")
print(result.group())





