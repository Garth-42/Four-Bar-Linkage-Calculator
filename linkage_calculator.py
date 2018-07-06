# -*- coding: utf-8 -*-

"""
I created the first version of this software when I was a student at Iowa State University.

Unfortunately, I accidentally deleted all of my versions of it when I was trying to hack together a pyhton script to backup my files... Oh the irony.

Welp, here we go.

I need a good project to start learning python and I want to rewrite this anyway. The code I wrote earlier was a complete mess.
"""


# jupyter and ipython version?

# Eventually use pipenv, git, spinx, and pytest, typing for this project in order to get familiar with proper coding documentation for larger proj
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# make this an int and do in radians...multiply by the decimal of accuracy want to get?
calc_interval = list(range(0,360)) #0 to 359 with 360 = 0

init_values = np.full(shape=(360),fill_value=np.nan,dtype=np.float)

d = {'link 1 Velocity': pd.Series(init_values, index = calc_interval[:]),
     'link 2': pd.Series(init_values, index = calc_interval[:]),
     'link 3': pd.Series(init_values, index = calc_interval[:]),
     'link 4': pd.Series(init_values, index = calc_interval[:])}

df = pd.DataFrame(d)
df.index.names = ['Angle']
s


# Create functions for retrieving and setting values in the dataframe? These would be good standalone modules?. (Or classes? Want easy syntax)
df.set_value(index=0,col='link 1 Velocity', value=555)

print(df.loc[0,'link 1 Velocity'])