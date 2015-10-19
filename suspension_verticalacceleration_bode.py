#!/usr/bin/env python
#http://python-control.sourceforge.net/manual/matlab_strings.html
#http://www.brown.edu/Departments/Engineering/Courses/En4/Notes/vibrations_forced/vibrations_forced.htm

'''
Graphs the frequency response (bode plot) of the output acceleration vs frequency

Approach: Assuming a worst case scenario roughness wavelength, critical velocity, omega_0, was fined tuned such that an attenuation of atleast -20dB occurrs at 0.13Ma (100 mph) and -5dB attenuation occurs at Mach1.
'''

from matplotlib.pyplot import * # Grab MATLAB plotting functions
from control.matlab import *    # MATLAB-like functions

######## Constants ########
pi = 3.14159265	# pi
g = 9.81	# gravitational constant (m/s^2)
Ma = 340.29	# Mach 1 (m/s)

######## Input: (Arbitrary) Parameters ########
#Note: The arbitrary parameters do not affect the frequency response diagram as they are merely used to calculate stiffness, k, and damping coeff, c, in conjunction with the critical design criteria
N = 12			# No. of suspensions
M_pod = 5000	# total pod mass in kg
m_pod = M_pod/N		# pod mass divided by N


######## Input: Critical Design Criteria ########
L_roughness = 200	# Estimated worst case scenario roughness wavelength of tube (m)
zeta = 0.25		# Damping ratio, 0.25 recommended for maximizing passenger comfort as per http://www.optimumg.com/docs/Springs%26Dampers_Tech_Tip_3.pdf
v_crit = 0.01*Ma	# Pod critical velocity (m/s)


######## Requirements Calcs ########
# Solve for req'd natural frequency (rad/s), given critical velocity and roughness wavelength
omega_0 = 2*pi*v_crit/L_roughness

# Solve for req'd suspension stiffness (N/m), given req'd natural frequency and pod mass
k_s = pow(omega_0,2)*m_pod/N

# Solve for req'd damping coefficient, given req'd suspension stiffness, pod mass, and damping ratio
c_s = zeta*(2*pow(k_s*m_pod/N,0.5))


#### Transfer function for tube deflection as input and vertical acceleration as output ####
G = tf([2*zeta*omega_0, pow(omega_0,2), 0, 0], [1, 2*zeta*omega_0, pow(omega_0,2)]); # Transfer function for vertical acceleration (output) against floor roughness (input)

'''
# Calculate natural frequency
omega_0 = pow(k_s/m_pod,0.5)
'''

f_0 = omega_0/(2*pi)
omega_Mach0_13 = 2*pi*0.13*Ma/L_roughness	# frequency at x Mach
omega_Mach1 = 2*pi*1*Ma/L_roughness	# frequency at x Mach

print "#### Input: Design Criteria ####"
print "v_crit (m/s) = ", v_crit
print "zeta = ", zeta
print

if zeta == 1:
	print "System is critically damped"
if zeta > 1:
	print "System is over-damped"
if zeta >= 0 and zeta < 1:
	print "System is under-damped"

print "#### Numeric calcs for reference ####"
print "v_crit (mph) = ", v_crit*2.23694
print "omega_0 (rad/s) = ", omega_0
print "omega_Mach0_13  (rad/s) = ", omega_Mach0_13
print "omega_Mach1  (rad/s) = ", omega_Mach1
print "omega_Mach2  (rad/s) = ", 2*omega_Mach1
print "Transfer function, G(s) = ", G

print "#### Output: Required Specs for Suspension ####"
print "k_s = ", k_s
print "c_s = ", c_s


'''
# Calculate natural frequency
omega_0 = pow(k_s*N/m_pod,0.5)
print "omega_0 = ", omega_0
print "f_0 = ", f_0
'''

figure('Hyperloop Suspension System - Frequency Response for Vertical Acceleration')
#G_ss = tf2ss(G)
#print G_ss
bode(G, dB=True)
#rlocus(G)

'''
figure('Hyperloop Suspension System - PZ Map')
pzmap(G)
'''

'''
# Only really necessary for assessing closed loop stability
figure('Hyperloop Suspension System - Nyquist Plot')
nyquist(G)
'''

show()

