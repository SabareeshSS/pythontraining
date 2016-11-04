'''
Created on 04-Nov-2016

@author: BALASUBRAMANIAM
'''
from PIL.ExifTags import GPSTAGS
class Vehicle:    
    #constructor
    def __init__(self,eng,whls,grs,mdl):
        self.engine=eng
        self.wheels=whls
        self.gears=grs
        self.model=mdl
        self.regNo=''
    
    def setRegNo(self,rNo):
        self.regNo=rNo
        
    def fetchData(self):
        if(len(self.regNo)>0): 
            print(self.model,self.engine,self.wheels,self.gears,self.regNo)
        else:
            print(self.model,self.engine,self.wheels,self.gears)  

#object created
car=Vehicle(234568,4,6,"Honda City")
bike=Vehicle(4378,2,3,"Yamaha FZ")
truck=Vehicle(34586837,8,5,"Eicher")
#using object call the method
print("Vehicle information without reg no")
car.fetchData()
bike.fetchData()
truck.fetchData()

print("Vehicle information with reg no")
car.setRegNo("TN-02-0646")
car.fetchData()


class AutomatedVehicle(Vehicle):
    def __init__(self,eng,whls,grs,mdl,gps,sensor):
        Vehicle.__init__(self, eng,whls,grs,mdl)
        self.GPS=gps
        self.Sensor=sensor
    def fetchData(self):
        Vehicle.fetchData(self)
        print(self.GPS,self.Sensor)
        

googleCar=AutomatedVehicle(24757,4,6,'Google-Car',True,True)
googleCar.fetchData()
googleCar.setRegNo("US-237457")
googleCar.fetchData()







