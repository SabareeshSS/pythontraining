'''
Created on 03-Jun-2016

@author: BALASUBRAMANIAM
'''
class Monitor:
    def __init__(self,brand,width,height,color):
        self.brand=brand
        self.width=width
        self.height=height
        self.color=color
    
    def display(self):
        print("Brand=%s"%(self.brand))
        print("Height=%s"%(self.height))
        print("Width=%s"%(self.width))
        print("Height=%s"%(self.color))
        
samsung = Monitor("Samsung",5,4,"Black")
samsung.display()
lg=Monitor("LG",5,5,"white")
lg.display()
