'''
Created on 03-Jun-2016

@author: BALASUBRAMANIAM
'''
class Product:
    def __init__(self,name,cost):
        self.name=name
        self.cost=cost
    def __radd__(self, othercost):
        return self.cost + othercost
    def __add__(self, othercost):
        return self.cost + othercost
obj1=Product("WM",30000)
obj2=Product("MW",12000)
print(sum([obj1,obj2]))
print(obj1+obj2)

