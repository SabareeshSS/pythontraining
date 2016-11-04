'''
Created on 01-Jun-2016

@author: BALASUBRAMANIAM
'''
import os
import glob
os.chdir('C:/Users/BALASUBRAMANIAM/')
print(os.getcwd())
metadata = os.stat('sanct.log')
print(metadata)

os.chdir('C:/Users/BALASUBRAMANIAM/WebstormProjects/AdvancedHTML5')

for f in glob.glob('*.html'):
    if os.stat(f).st_size > 60:
        print(f)
        
        
