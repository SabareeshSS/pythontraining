'''
Created on 04-Nov-2016

@author: BALASUBRAMANIAM
'''
from xml.dom import minidom

doc=minidom.parse("EmployeeData.xml")
emps = doc.getElementsByTagName("Employee")
for emp in emps:
    name=emp.getAttribute("name")
    location=emp.getElementsByTagName("Location")[0]
    phoneno1 = emp.getElementsByTagName("MobileNo")[0]
    phoneno2 = emp.getElementsByTagName("MobileNo")[1]
    print(name,location.firstChild.data,phoneno1.firstChild.data,phoneno2.firstChild.data)
