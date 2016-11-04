'''
Created on 03-Jun-2016

@author: BALASUBRAMANIAM
'''
import calendar

c = calendar.TextCalendar(calendar.SUNDAY)
c.prmonth(2016, 11)


print (calendar.TextCalendar(calendar.SUNDAY).formatyear(2016, 2, 1, 1, 2))