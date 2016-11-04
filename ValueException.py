'''
Created on 02-Nov-2016

@author: BALASUBRAMANIAM
'''
while True:
    try:
       x = int(input("Please enter a number: "))
       break
    except ValueError:
         print("Oops!  That was no valid number.  Try again...")