'''
Created on 02-Jun-2016

@author: BALASUBRAMANIAM
'''

employees={
           '145':{'Name':'Ashok','Project':'Automation','SkillSet':['C','C++']},
           '187':{'Name':'Anjana','Project':'Quality','SkillSet':['C','C++','Java']},
           '223':{'Name':'Sharuk','Project':'Testing','SkillSet':['C','C++','Python']},
           '345':{'Name':'Buvana','Project':'Training','SkillSet':['C','C++','Perl']}          
           
           }
searchkey=input("Enter Employee id")

for _ in employees:
    if (_==searchkey):
        
        for result in employees.get(_):
            print("%s:\t%s" %(result,employees[_][result]))  
        
