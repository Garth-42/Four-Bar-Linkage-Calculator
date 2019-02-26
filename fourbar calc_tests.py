# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 22:30:02 2019

@author: garth
"""

import matplotlib.pyplot as plt
import math

def plotLinkage(a_x, a_y, b_x, b_y, link_d):
    d_x = link_d
    d_y = 0
    plt.plot( [ 0  , a_x ], [ 0  , a_y ] )
    plt.plot( [ a_x, b_x ], [ a_y, b_y ] )
    plt.plot( [ b_x, d_x ], [ b_y, d_y ] )
    #plt.savefig("out")

fig = plt.figure()
theta2 = math.radians(40)
a=40
b=120
c=80
d=100
# Don't use atan2? P176
#Do these once for a simulation (theta2 doesnt change these parameters)



k1 = d/a
k2 = d/c
k3 = ( math.pow(a,2) - math.pow(b,2) + math.pow(c,2) + math.pow(d,2) ) / ( 2*a*c )

A = math.cos(theta2) - k1 - k2*math.cos(theta2) + k3
B = -2*math.sin(theta2)
C = k1 - (k2 + 1)*math.cos(theta2) + k3

theta4Open = 2*math.atan( ( -B - math.sqrt( math.pow(B,2) - 4*A*C ) ) / (2*A) )
theta4Cross = 2*math.atan( ( -B + math.sqrt( math.pow(B,2) - 4*A*C ) ) / (2*A) )

#do these once as well
k4 = d/b
k5 = ( math.pow(c,2) - math.pow(d,2) - math.pow(a,2) - math.pow(b,2) ) / ( 2*a*b )

D = math.cos(theta2) - k1 + k4*math.cos(theta2) + k5
E = -2*math.sin(theta2)
F = k1 + (k4 - 1)*math.cos(theta2) + k5

theta3Open = 2*math.atan( ( -E - math.sqrt( math.pow(E,2) - 4*D*F ) ) / (2*D) )
theta3Cross = 2*math.atan( ( -E + math.sqrt( math.pow(E,2) - 4*D*F ) ) / (2*D) )

# By convention used
d_x = d
d_y = 0

a_x = a*math.cos(theta2)
a_y = a*math.cos(theta2)

b_x_Open = a_x + b*math.cos(theta3Open)
b_y_Open = a_y + b*math.sin(theta3Open)

b_x_Cross = a_x + b*math.cos(theta3Cross)
b_y_Cross = a_y + b*math.sin(theta3Cross)

#c_x_Open = d_x + c*math.cos(theta4Open)
#c_y_Open = d_y + c*math.sin(theta4Open)

#c_x_Cross = d_x + c*math.cos(theta4Cross)
#c_y_Cross = d_y + c*math.sin(theta4Cross)

plotLinkage(a_x = a_x, a_y = a_y, b_x = b_x_Open, b_y = b_y_Open, link_d = d)
plotLinkage(a_x = a_x, a_y = a_y, b_x = b_x_Cross, b_y = b_y_Cr)