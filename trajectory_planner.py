import numpy as np          #Extracting Numpy for generating arrays from csv
import pandas as pd         #Pandas for using csv
from matplotlib.pyplot import *     #Pyplot for plotting results
from scipy.spatial import Delaunay      #Delaunay method for interpolation
from scipy.signal import lti, step2     #Functions for state space modeling
from control.matlab import *            #Matlab Functions
import matplotlib.patches as mp
import csv
import re
import sys
import os


def read_data():

    #Extracting data into arrays from csv
    #s = serial no, name = load point, v = velocity, h = height of gap
    #F_d = Drag force, F_l = force of lift, qsm = Mean heat flux on the surface of the I-beam, qsmx = Max heat flux on I-beam
    s, name, v, h = np.loadtxt(open("ebd.csv", "rb"), delimiter = ',', skiprows = 1, usecols = (0, 1, 2, 3), unpack = True)
    F_d, F_l, qsm, qsmx = np.loadtxt(open("ebd.csv", "rb"), delimiter = ',', skiprows = 1, usecols = (4, 5, 6, 7), unpack = True)

#Input Modular force objects
#Pusher force, F_p
#Hover motor force, F_m
#Lateral stabilization force, F_ls
#Aero drag force, F_d
#Eddy brake force, F_eb
#Acceleration = (sum of forces)/M_pod
