#!/usr/bin/env python
# reference:Analysis of a Channeled Centerbody Supersonic Inlet for F-15B Flight Research
# by A. Ratnayake

import math
import numpy as np
try:
    r_t = input("What is the radius of tube?")
except:
    print "Please enter a numeric value"
    r_t = input("What is the radius of tube?")

try:
    r_p = input("What is the radius of pod?")
except:
    print "Please enter a numeric value"
    r_p = input("What is the radius of pod?")
try:
    v = input("What is the velocity of pod?")
except:
    print "Please enter a numeric value in metres per second"
    v = input("What is the velocity of pod?")

G = 1.4   #Gamma
pi = 3.14 #Pi
A_t = pi*r_t*r_t #Area of tube
A_p = pi*r_p*r_p #Area of pod
A_b = A_t - A_p #Area of bypass/passage
a = 340 #Speed of sound in the medium
M = v/a

A_ratio = (A_b/A_t) #Ratio of area

O_1 = pow((G-1)/(G+1), 0.5) #Operator 1

O_2_1 = ((2*G)/(G+1))
O_2_2 = (1/(G-1))

O_2 = pow(O_2_1, O_2_2) #Operator 2

O_3_1 = (2/(G-1))
O_3_2 = np.power(M, -2)
O_3_3 = (1+(O_3_1*O_3_2))

O_3 = pow(O_3_3, 0.5) #Operator 3

O_4_1 = ((G-1)/(2*G))
O_4_2 = (1-((O_4_1)*(O_3_2)))

O_4 = np.power((O_4_2+0j), O_2_2) #Operator 4

RHS = O_1*O_2*O_3*O_4 #Right hand side of the equation

if A_ratio == RHS:
    print "Design feasible with Kantrowitz"
else:
    print "Design not feasible with Kantrowitz"
