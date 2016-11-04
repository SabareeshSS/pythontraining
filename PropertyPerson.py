'''
Created on 03-Jun-2016

@author: BALASUBRAMANIAM
'''
class Person:
    def __init__(self, height):
        self.height = height

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height

jane = Person(153) # Jane is 153cm tall

jane.height += 1 # Jane grows by a centimetre
jane.set_height(jane.height + 1) # Jane grows again