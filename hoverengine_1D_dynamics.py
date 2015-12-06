#!/usr/bin/env python

from matplotlib.pyplot import * # Grab MATLAB plotting functions
import matplotlib.patches as mpatches
from control.matlab import *    # MATLAB-like functions
import numpy as pod
from scipy.signal import lti, step2

# Assumptions: 
# neglect mass of springs itself
# neglect any external viscous forces

# Notes: multiple C & D state space variables were used since numpy library can't handle multi-output

######## Constants ########
pi = 3.14159265	# pi
g = 9.81	# gravitational constant (m/s^2)
Ma = 340.29	# Mach 1 (m/s)
e = 2.71828183	# Euler's No.

######## Unsprung System (State Space Analysis) ########
#   _________
#  |         |
#  |  m_pod  |    ^ x_pod
#  |_________|   _| 
#       |        
#  k_h  Z         ^ r
#   ____|____    _|
#
#
# State variables: x = [x1, x2] = [x_pod, x_pod_dot]
# Input variables: u = [u1] = [r], road reference
# Output variables: y = [y1] = [a_pod], pod vertical acceleration

#### Physical Parameters for Unsprung System ####
N = 8.			# No. of hover units
M_pod = 200.		# total pod mass (kg)
m_pod = M_pod/N		# pod mass divided by No. of hover units
k_h = 24701		# Approximate stiffness of ArxPax hoverboard for 10mm hover height

A = pod.array([	[	0,		1	],
		[	-k_h/m_pod,	0	] ])

B = pod.array([	[	0		],
		[	k_h/m_pod	] ])


C_x_pod = pod.array([ [	1,	0	] ])	# C matrix for pod travel output

D_x_pod = pod.array([ [	0 ] ])			# D matrix for pod travel output


C_x_hovergap = pod.array([	[	1,	0	]	])	# C matrix for hover gap output

D_x_hovergap = pod.array([	[	-1	]	 ])		# D matrix for hover gap output


C_a_pod = pod.array([	A[1,:]	 ])	# C matrix for acceleration output

D_a_pod = pod.array([	B[1,:]	 ])	# D matrix for acceleration output


#### Frequency Domain Properties ####
omega_0_unsprung = pow(k_h/m_pod,0.5)			# Natural frequency (for unsprung system)
v_cruise = 0.13*Ma					# Cruising velocity (m/s)
L_roughness_unsprung = 2*pi*v_cruise/omega_0_unsprung	# Pod's critical roughness wavelength (m)

#### Transfer function(s) for unsprung system ####
sys_unsprung_tf_a_pod = ss2tf(A,B,C_a_pod,D_a_pod)	# Transfer function for pod acceleration
#sys_unsprung_tf_a_pod = tf([0, pow(omega_0_unsprung,2), 0, 0], [1, 0, pow(omega_0_unsprung,2)]); # Transfer function for vertical acceleration (output) against floor roughness (input)

#### LTI model for sprung system ####
sys_unsprung_lti = lti(A,B,C_x_pod,D_x_pod)
sys_unsprung_lti_hovergap = lti(A,B,C_x_hovergap,D_x_hovergap)


######## Sprung System (State Space Analysis) ########
#   _________
#  |         |
#  |  m_pod  |    ^ x_pod
#  |_________|   _| 
#     |   |
#  k  Z  |-|  c
#   __|___|__
#  | m_hover |    ^ x_hoverengine
#  |_________|   _|
#       |        
#  k_h  Z         ^ r
#   ____|____    _|
#
# State variables: x = [x1, x2, x3, x4] = [x_pod, x_pod_dot, x_hoverboard, x_hoverboard_dot]
# Input variables: u = [u1] = [r], road reference
# Output variables: y = [y1, y2, y3], where pod vertical travel, x_pod = y1; hover gap, x_hovergap = x_hoverengine - r = y2; pod vertical acceleration, a_pod = y3.

#### Physical Parameters for Sprung System ####
N = 8.			# No. of hover units
m_hover = 7.		# Hover engine weight (kg)
M_pod = 200.-m_hover*N	# pod mass (kg)
m_pod = M_pod/N		# pod mass divided by No. of hover units
k = 372144.			# Spring stiffness of 51507-4 isolator (N/m)
c = 0.			# Damping coefficient (N*s/m)
k_h = 24701		# Approximate stiffness of ArxPax hoverboard for 10mm hover height

A = pod.array([	[	0,			1,			0,			0		],
		[	-k/m_pod,		-c/m_pod,		k/m_pod,		c/m_pod		],
		[	0,			0,			0,			1		],
		[	k/m_hover,		c/m_hover,		-(k+k_h)/m_hover,	-c/m_hover	] ])

B = pod.array([	[	0		],
		[	0		],
		[	0		],
		[	k_h/m_hover	] ])

C_x_pod = pod.array([ [	1,	0,	0,	0] ])	# C matrix for pod travel output

D_x_pod = pod.array([ [	0 ] ])	# D matrix for pod travel output


C_x_hovergap = pod.array([	[	0,	0,	1,	0	]	])	# C matrix for hover gap output

D_x_hovergap = pod.array([	[	-1	]	 ])	# D matrix for hover gap output


C_a_pod = pod.array([	A[1,:]	 ])	# C matrix for acceleration output

D_a_pod = pod.array([	B[1,:]	 ])	# D matrix for acceleration output


I = pod.array([	[1, 0, 0, 0],
		[0, 1, 0, 0],
		[0, 0, 1, 0],
		[0, 0, 0, 1]	])

#### State space representation(s) for sprung system ####
sys_sprung_ss_x_pod = ss(A,B,C_x_pod,D_x_pod)			# Transfer function representation of sprung system
sys_sprung_ss_x_hovergap = ss(A,B,C_x_hovergap,D_x_hovergap)		# Transfer function representation of sprung system

#### Transfer function(s) for sprung system ####
sys_sprung_tf_a_pod = ss2tf(A,B,C_a_pod,D_a_pod)	# Transfer function for pod acceleration

#### LTI model for sprung system ####
sys_sprung_lti = lti(A,B,C_x_pod,D_x_pod)
sys_sprung_lti_hovergap = lti(A,B,C_x_hovergap,D_x_hovergap)

print 
print "#### Numeric calcs for reference ####"
print "v_cruise (m/s) = ", v_cruise
print "omega_0_unsprung (rad/s) = ", omega_0_unsprung
print "critical roughness wavelength (for unsprung sys) = ", L_roughness_unsprung
print "Transfer function for unsprung system = ", sys_unsprung_tf_a_pod
print "Transfer function, sys_sprung_tf_a_pod = ", sys_sprung_tf_a_pod

print "#### Physical Parameters of system ####"
print "No. of hover units = ", N
print "Hover-engine weight (kg) = ", m_hover
print "pod mass (kg) = ", M_pod
print "pod mass divided by No. of hover units (kg) = ", m_pod
print "k (N/m) = ", k
print "c (N*s/m) = ", c
print "k_h (N/m) = ", k_h


figure('Hyperloop HoverEngine - pod acceleration output ')
bode(sys_unsprung_tf_a_pod, sys_sprung_tf_a_pod, dB=True)


#figure('Hyperloop HoverEngine - pod travel output ')
#lsim(sys_unsprung_tf_a_pod, U=0.0, T=None, X0=0.0)


'''
figure('Hyperloop HoverEngine - pod hovergap output (step response, unsprung system)')
t, y = step2(sys_unsprung_lti_hovergap)
plot(t, y)

figure('Hyperloop HoverEngine - pod travel output (step response, sprung system)')
t, y = step2(sys_sprung_lti)
ylim(-1, 1)
xlim(0, 10000)
plot(t, y)

figure('Hyperloop HoverEngine - pod hovergap output (step response, sprung system)')
t, y = step2(sys_sprung_lti_hovergap)
ylim(-3, 3)
xlim(0, 10000)
plot(t, y)

legend(loc=2)
'''

show()


# References:
# http://python-control.sourceforge.net/manual/matlab_strings.html
# http://www.brown.edu/Departments/Engineering/Courses/En4/Notes/vibrations_forced/vibrations_forced.htm
# http://www.mathworks.com/help/robust/gs/active-suspension-control-design.html
# Damping ratio, 0.25 recommended for maximizing passenger comfort as per http://www.optimumg.com/docs/Springs%26Dampers_Tech_Tip_3.pdf

