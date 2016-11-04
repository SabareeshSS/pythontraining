'''
Created on 02-Nov-2016

@author: BALASUBRAMANIAM
'''
import sys
import logging
logging.basicConfig(filename='testfile.log',level=logging.DEBUG)
try:
    f = open('info123.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    logging.error("OS error: {0}".format(err))
except ValueError:
    logging.error("Could not convert data to an integer.")
except:
    logging.error("Unexpected error:", sys.exc_info()[0])
    raise