'''
Created on 02-Jun-2016

@author: BALASUBRAMANIAM
'''
from xml.dom import minidom

doc = minidom.parse("country.xml")
countries = doc.getElementsByTagName("country")
for country in countries:
        name = country.getAttribute("name")
        rank = country.getElementsByTagName("rank")[0]
        year = country.getElementsByTagName("year")[0]
        gdppc=  country.getElementsByTagName("gdppc")[0]
        print("id:%s, rank:%s, year:%s, gdppc:%s" %
              (name, rank.firstChild.data, year.firstChild.data,gdppc.firstChild.data))