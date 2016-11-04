'''
Created on 03-Jun-2016

@author: BALASUBRAMANIAM
'''
class Employee:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def set_email(self,email):
        self.email=email
    def set_mobileNo(self,mobileNo):
        self.mobileNo=mobileNo
    def get_email(self):
        return self.email    
    def get_mobileNo(self):
        return self.mobileNo
    def display(self):
        print("Employee Id=%d"%(self.id))
        print("Name=%s"%(self.name))
    
arun=Employee(67,"Arun")
arun.display()
arun.set_email("arun@bosch.com")
arun.set_mobileNo(99520474747)
print(arun.get_email())


class Manager(Employee):
    def __init__(self,id,name,allowance):
        Employee.__init__(self, id, name)
        self.allowance=allowance
        
    def display(self):
        Employee.display(self)
        print("Allowance=%s"%(self.allowance))
        


hema = Manager(78,"Hema",20000)
hema.display()
hema.set_email("hema@bosch.com")
print(hema.get_email())

