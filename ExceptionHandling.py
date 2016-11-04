'''
Created on 04-Nov-2016

@author: BALASUBRAMANIAM
'''
import logging
logging.basicConfig(filename='Vehicle.log',level=logging.DEBUG)
try:
    engineNo=int(input("Enter Engine No"))
    logging.info(str(engineNo))   
   
except ValueError:
        logging.error("Value is not a number")
       
    
