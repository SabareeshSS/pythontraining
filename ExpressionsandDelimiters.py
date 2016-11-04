'''
Created on 01-Jun-2016

@author: BALASUBRAMANIAM
'''
import re
message='Beautiful, is; better*than\nugly'
print(re.split(';|,|\*|\n',message))


