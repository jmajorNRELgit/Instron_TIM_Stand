# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 08:45:06 2019

@author: jmajor
"""


import pandas as pd
import os
import time
import copy

start = time.time()

#try:
#    os.remove('DAQ_data.txt')
#except:
#    pass

for i in range(100000):

    temp_data = '1,2,3,4,5,6,7,8\n'

    with open('DAQ_data.txt', 'a') as f:
        if os.stat('DAQ_data.txt').st_size == 0: #if the data file is empty this adds the headers
            f.write('Time(s),STD,One,Two,Three,Four,Five,Six\n')
            f.write(temp_data)
        else:
            f.write(temp_data)

    df = pd.read_csv('DAQ_data.txt')

print(time.time() - start)


x = copy.deepcopy(df)

def rea():
    df = pd.read_csv('DAQ_data.txt')

def re():
    y = copy.deepcopy(x)
