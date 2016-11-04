'''
Created on 04-Nov-2016

@author: BALASUBRAMANIAM
'''
from xml.dom import minidom

doc=minidom.Document()

products = doc.createElement("Products")
doc.appendChild(products)
product1 = doc.createElement("Product")
id=doc.createElement("Id")
data=doc.createTextNode("32477")
id.appendChild(data)
product1.appendChild(id)
name=doc.createElement("name")
data=doc.createTextNode("Wheel")
name.appendChild(data)
product1.appendChild(name)
cost=doc.createElement("cost")
data=doc.createTextNode("6000")
cost.appendChild(data)
product1.appendChild(cost)
products.appendChild(product1)
product2 =doc.createElement("Product")
id=doc.createElement("Id")
data=doc.createTextNode("32480")
id.appendChild(data)
product2.appendChild(id)
name=doc.createElement("name")
data=doc.createTextNode("Bumper")
name.appendChild(data)
product2.appendChild(name)
cost=doc.createElement("cost")
data=doc.createTextNode("1200")
cost.appendChild(data)
product2.appendChild(cost)
products.appendChild(product2)

xml_str = doc.toprettyxml(indent="  ")
with open("Products.xml", "w") as f:
    f.write(xml_str)
