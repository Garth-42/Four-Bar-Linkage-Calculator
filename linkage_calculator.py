# -*- coding: utf-8 -*-

"""
I created the first version of this software when I was a student at Iowa State University.

Unfortunately, I accidentally deleted all of my versions of it when I was trying to hack together a pyhton script to backup my files... Oh the irony.

Welp, here we go.

I need a good project to start learning python and I want to rewrite this anyway. The code I wrote earlier was a complete mess.
"""


#jupyter and ipython version?

# Eventually use pipenv, git, spinx, and pytest, typing for this project in order to get familiar with proper coding documentation for larger proj
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


'''
d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
data_frame = pd.DataFrame(d)
'''

calc_interval = list(range(0,360)) #0 to 359 with 360 = 0
#make this an int and do in radians...multiply by the decimal of accuracy want to get?
"""
d = {'link 1' : pd.Series(np.zeros(360) ), index = calc_interval[]),
     'link 2' : pd.Series(np.zeros(360) ), index = calc_interval[]),
     'link 3' : pd.Series(np.zeros(360) ), index = calc_interva[]),
     'link 4' : pd.Series(np.zeros(360) ), index = calc_interval[])}
data_frame = pd.DataFrame(d)
"""
this_is_array = np.full(shape=(360),fill_value=np.nan,dtype=np.float)

d = {'one' : pd.Series(this_is_array, index=calc_interval[:]),
     'two' : pd.Series(list(range(360)), index=calc_interval[:])}
data_frame = pd.DataFrame(d)
data_frame.index.names = ['Angle']

