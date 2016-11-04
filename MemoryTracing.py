'''
Created on 01-Jun-2016

@author: BALASUBRAMANIAM
'''

import gc
gc.collect()  # don't care about stuff that would be garbage collected properly
import objgraph
objgraph.show_most_common_types()