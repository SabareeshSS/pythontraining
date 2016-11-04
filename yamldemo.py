'''
Created on 02-Jun-2016

@author: BALASUBRAMANIAM
'''
import yaml

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)
dictdata={}
for section in cfg:
    print (section)
    dictdata[section]=cfg[section]
    print(cfg[section])
print (dictdata)

for _ in dictdata:
    print(_)
    
    
#print(cfg['mysql'])
#print(cfg['other'])