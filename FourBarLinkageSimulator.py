# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 23:01:38 2019

@author: garth

Code Overview:
This program takes a four-bar linkage as input and outputs a gif of the crossed and open configurations of the linkage.

TODO:
Add warning for an impossible link so an impossible link isn't attempted to be calculated in the simulation function
Refactor to be more idiomatic
Refactor to be used as a library
Add a README explaining convention/etc.
"""

import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import imageio as io
import os
#keeps plotting a graph and presenting to user. how stop doing that?

def positionSimulation(a, b, c, d, step = .05):
    # Vectorized Calculation for Position over a rotation
    startAngle = 0
    stopAngle = 2*math.pi

    theta2 = np.arange(start = startAngle, stop = stopAngle, step = step)
    zeros = np.zeros(theta2.size)
    dataSeries = {'A':zeros, 'B': zeros, 'C':zeros, 'D':zeros, 'E':zeros, 'F':zeros,
         'theta2': theta2, 'theta4Open': zeros, 'theta4Crossed': zeros,
         'theta3Open': zeros, 'theta3Crossed': zeros, 'b_x_Open': zeros, 'b_y_Open': zeros, 'b_x_Crossed': zeros, 'b_y_Crossed': zeros }
    df = pd.DataFrame(data=dataSeries)

    #Do these once for a simulation (theta2 doesnt change these parameters)
    k1 = d/a
    k2 = d/c
    k3 = ( math.pow(a,2) - math.pow(b,2) + math.pow(c,2) + math.pow(d,2) ) / ( 2*a*c )
    k4 = d/b
    k5 = ( math.pow(c,2) - math.pow(d,2) - math.pow(a,2) - math.pow(b,2) ) / ( 2*a*b )

    # Scalar math to the matrix
    df['A'] = (np.cos(df['theta2']) - k1 - k2*np.cos(df['theta2']) + k3)
    # df B is true to value...
    df['B'] = (-2*np.sin(df['theta2']))
    df['C'] = (k1 - (k2 + 1)*np.cos(df['theta2']) + k3)

    df['theta4Open'] = 2*np.arctan( ( -df['B'] - np.sqrt( np.power(df['B'],2) - 4*df['A']*df['C'] ) ) / (2*df['A']) )
    df['theta4Crossed'] = 2*np.arctan( ( -df['B'] + np.sqrt( np.power(df['B'],2) - 4*df['A']*df['C'] ) ) / (2*df['A']) )

    df['D'] = np.cos(theta2) - k1 + k4*np.cos(theta2) + k5
    df['E'] = -2*np.sin(theta2)
    df['F'] = k1 + (k4 - 1)*np.cos(theta2) + k5

    df['theta3Open'] = 2*np.arctan( ( -df['E'] - np.sqrt( np.power(df['E'],2) - 4*df['D']*df['F'] ) ) / (2*df['D']) )
    df['theta3Crossed'] = 2*np.arctan( ( -df['E'] + np.sqrt( np.power(df['E'],2) - 4*df['D']*df['F'] ) ) / (2*df['D']) )
    #df.loc[df['theta2']== .698]
    #df.loc[689]

    df['a_x'] = a*np.cos(df['theta2'])
    df['a_y'] = a*np.sin(df['theta2'])

    df['b_x_Open'] = df['a_x'] + b*np.cos(df['theta3Open'])
    df['b_y_Open'] = df['a_y'] + b*np.sin(df['theta3Open'])

    df['b_x_Crossed'] = df['a_x'] + b*np.cos(df['theta3Crossed'])
    df['b_y_Crossed'] = df['a_y'] + b*np.sin(df['theta3Crossed'])

    #df['c_x'] = df['d_x'] + c*math.cos(theta4Open)
    #df['c_y'] = df['d_y'] + c*math.sin(theta4Open)
    #seeing if this == b_x could be a test for the code?
    
    # Don't put constant info in the dataframe
    #df['d_x'] = d
    #df['d_y'] = 0

    return df

def plotLinkage(a_x, a_y, b_x, b_y, link_d, openOrCross):
    d_x = link_d
    d_y = 0
    plt.plot( [ 0  , a_x ], [ 0  , a_y ] ) # Semicolon suppresses output?
    plt.plot( [ a_x, b_x ], [ a_y, b_y ] )
    plt.plot( [ b_x, d_x ], [ b_y, d_y ] )
    
def makePictures(df, d, openOrCrossed):
    
    i = 1000
    fig = plt.figure()
    if openOrCrossed == 'open':
        minValuesX = [0, df['a_x'].min(),df['b_x_Open'].min(), d]
        minValuesY = [0, df['a_y'].min(),df['b_y_Open'].min()]
        minValueX = min(minValuesX)
        minValueY = min(minValuesY)
        maxValuesX = [0, df['a_x'].max(),df['b_x_Open'].max(), d]
        maxValuesY = [0, df['a_y'].max(),df['b_y_Open'].max()]
        maxValueX = max(maxValuesX)
        maxValueY = max(maxValuesY)
        
        for row in df.itertuples():
            plt.clf()
            ax = fig.add_subplot(1,1,1)
            plotLinkage( getattr(row, 'a_x'), getattr(row,'a_y'), getattr(row, 'b_x_Open'), getattr(row, 'b_y_Open'), link_d = d, openOrCross = 'open')
            ax.axis('scaled')
            ax.set_xlim([minValueX,maxValueX]);
            ax.set_ylim([minValueY, maxValueY]);
            plt.savefig('fourbar_pics_open/'+'open' + str(i) + '.png')
            i = i + 1
            
    elif openOrCrossed == 'crossed':
        minValuesX = [0, df['a_x'].min(),df['b_x_Crossed'].min(), d]
        minValuesY = [0, df['a_y'].min(),df['b_y_Crossed'].min()]
        minValueX = min(minValuesX)
        minValueY = min(minValuesY)
        maxValuesX = [0, df['a_x'].max(),df['b_x_Crossed'].max(), d]
        maxValuesY = [0, df['a_y'].max(),df['b_y_Crossed'].max()]
        maxValueX = max(maxValuesX)
        maxValueY = max(maxValuesY)
        for row in df.itertuples():
            plt.clf()
            ax = fig.add_subplot(1,1,1)
            plotLinkage( getattr(row, 'a_x'), getattr(row,'a_y'), getattr(row, 'b_x_Crossed'), getattr(row, 'b_y_Crossed'), link_d = d, openOrCross = 'cross')
            ax.axis('scaled')
            ax.set_xlim([minValueX,maxValueX]);
            ax.set_ylim([minValueY, maxValueY]);
            plt.savefig('fourbar_pics_crossed/'+'crossed' + str(i) + '.png')
            i = i + 1

def makeGif(openOrCrossed):
    # https://stackoverflow.com/questions/41228209/making-gif-from-images-using-imageio-in-python
    #making animation
    
    if openOrCrossed == 'open':
        with io.get_writer('./fourbar_pics_open/Grashof1.gif', mode='I', duration =.03) as writer:#past limit of function. need to decrease calc steps
            file_names = sorted((fn for fn in os.listdir('./fourbar_pics_open') if fn.startswith('open')))
            for filename in file_names:
                image = io.imread('./fourbar_pics_open/' + filename)
                writer.append_data(image)
        writer.close()
    
    elif openOrCrossed == 'crossed':
        with io.get_writer('./fourbar_pics_crossed/Grashof1.gif', mode='I', duration = .03) as writer:
            file_names = sorted((fn for fn in os.listdir('./fourbar_pics_crossed') if fn.startswith('crossed')))
            for filename in file_names:
                image = io.imread('./fourbar_pics_crossed/' + filename)
                writer.append_data(image)
        writer.close()

def main():
    
    # Inputs
    # These are the length values of links A, B, C, and D respectively.
    a=60
    b=120
    c=80
    d=100
    
    df = positionSimulation(a,b,c,d)
    makePictures(df, d, 'open')
    makeGif("open")
    makePictures(df, d, 'crossed')
    makeGif("crossed")

if __name__ == "__main__":
    main()