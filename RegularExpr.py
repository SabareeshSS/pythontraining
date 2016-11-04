'''
Created on 01-Jun-2016

@author: BALASUBRAMANIAM
'''
import re

#to find starting with
result = re.match(r'AV', 'AV Analytics Vidhya AV')
print (result)

result = re.match(r'AV', 'AV Analytics Vidhya AV')
print (result.group(0))
result = re.match(r'Analytics', 'AV Analytics Vidhya AV')
print (result)
#he start and end position of matching pattern in the string.
result = re.match(r'AV', 'AV Analytics Vidhya AV')
print (result.start())
print (result.end())
result = re.search(r'Analytics', 'AV Analytics Vidhya AV')
print (result.group(0))

result = re.findall(r'AV', 'AV Analytics Vidhya AV')
print (result)

#splits by occurrence
result=re.split(r'y','Analytics')
print(result)

result=re.split(r'i','Analytics Vidhya')
print (result)

result=re.split(r'i','Analytics Vidhya',maxsplit=1)
print (result)

#re.sub(pattern, repl, string)
#replace the pattern
result=re.sub(r'India','the World','AV is largest Analytics community of India')
print (result)


pattern=re.compile('AV')
result=pattern.findall('AV Analytics Vidhya AV')
print (result)
result2=pattern.findall('AV is largest analytics community of India')
print (result2)

#findall by each character\w

result=re.findall(r'\w','AV is largest Analytics community of India')
print (result)
#extract by word
result=re.findall(r'\w*','AV is largest Analytics community of India')
print (result)
#Extract each word ^
result=re.findall(r'^\w+','AV is largest Analytics community of India')
print (result)
#Return the first two character as word
result=re.findall(r'\w\w','AV is largest Analytics community of India')
print (result)

#first two letters from word boundary
result=re.findall(r'\b\w.','AV is largest Analytics community of India')
print (result)

#Extract all characters after @
result=re.findall(r'@\w+','abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz') 
print (result)

result=re.findall(r'@\w+.\w+','abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
print (result)

result=re.findall(r'@\w+.(\w+)','abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
print (result)

#return date
result=re.findall(r'\d{2}-\d{2}-\d{4}','Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
print (result)
#extract only year
result=re.findall(r'\d{2}-\d{2}-(\d{4})','Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
print (result)

#return each word
result=re.findall(r'\w+','AV is largest Analytics community of India')
print (result)

#return each word with vowel

result=re.findall(r'\b[aeiouAEIOU]\w+','AV is largest Analytics community of India')
print (result)


li=['9999999999','999999-999','99999x9999']
for val in li:
    if re.match(r'[8-9]{1}[0-9]{9}',val) and len(val) == 10:
        print ('yes')
    else:
        print ('no')
     

line = 'asdf fjdk;afed,fjek,asdf,foo' 
# String has multiple delimiters (";",","," ").
result= re.split(r'[;,\s]', line)
print (result)




t="A fat cat doesn't eat oat but a rat eats bats."
mo = re.findall("[force]at", t)
print(mo)

items = re.findall("([0-9]+).*: (.*)", "Customer number: 232454, Date: February 12, 2011")
print(items)
s = '100 NORTH MAIN ROAD'
#s=s.replace('ROAD', 'RD.')
s=re.sub('ROAD$', 'RD.', s)
print(s)

phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
print(phonePattern.search('800-555-1212').groups())

#D for character match
phonePattern = re.compile(r'^(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
print(phonePattern.search('80055512121234').groups())
print(phonePattern.search('800.555.1212 x1234').groups())

phonePattern = re.compile(r'^\D*(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
print(phonePattern.search('(800)5551212 ext. 1234').groups())
print(phonePattern.search('Work-d (800)- 555.1212 #1234').groups())
"""
phonePattern = re.compile(r'''
# don't match beginning of string, number can start anywhere
(\d{3}) # area code is 3 digits (e.g. '800')
\D* # optional separator is any number of non-digits
(\d{3}) # trunk is 3 digits (e.g. '555')
\D* # optional separator
(\d{4}) # rest of number is 4 digits (e.g. '1212')
\D* # optional separator
(\d*) # extension is optional and can be any number of digits
$ # end of string
''', re.VERBOSE)"""

phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')

print(phonePattern.search('work 1-(800) 555.1212 #1234').group(1))
