#!/usr/bin/env python
#http://python-control.sourceforge.net/manual/matlab_strings.html
#http://www.brown.edu/Departments/Engineering/Courses/En4/Notes/vibrations_forced/vibrations_forced.htm

from matplotlib.pyplot import * # Grab MATLAB plotting functions
from control.matlab import *    # MATLAB-like functions

######## Constants ########
pi = 3.14159265	# pi
g = 9.81	# gravitational constant (m/s^2)
Ma = 340.29	# Mach 1 (m/s)

######## Input parameters ########
N = 6		# No. of suspensions
m_pod = 5000/N	# 5000 kg pod divided by N
L_tube_section = 200	# Length between pylons (m) - Awaiting per SpaceX tube spec release

# Roughness wavelength of tube (Assumed to occur at 1st harmonic frequency)
L_roughness = L_tube_section	# Length between pylons (m)


######## Design Criteria ########
v_crit = 0.01*Ma	# Critical Speed at which maximum amplitude of vibration occurs (m/s)
zeta = 0.4	# Damping ratio (tentative value. Modern control textbooks recommend setting zeta small, but not too small)


######## Calculated Requirements ########
# Solve for req'd natural frequency (rad/s), given critical velocity
omega_0 = 2*pi*v_crit/L_roughness

# Solve for req'd suspension stiffness (N/m), given req'd natural frequency
k_s = pow(omega_0,2)*m_pod/N

# Solve for req'd damping coefficient, given req'd suspension stiffness
c_s = zeta*(2*pow(k_s*m_pod/N,0.5))


#### LTI Model ####
G = tf([c_s, k_s], [m_pod/N, c_s, k_s]); # Transfer function, G(s) = X_pod(s)/X_tube(s)

'''
# Calculate natural frequency
omega_0 = pow(k_s/m_pod,0.5)
'''

f_0 = omega_0/(2*pi)
omega_Mach0_13 = 2*pi*0.13*Ma/L_roughness	# frequency at x Mach
omega_Mach1 = 2*pi*1*Ma/L_roughness	# frequency at x Mach

print "v_crit = ", v_crit
print "v_crit_mph = ", v_crit*2.23694
print "zeta = ", zeta

if zeta == 1:
	print "System is critically damped"
if zeta > 1:
	print "System is over-damped"
if zeta >= 0 and zeta < 1:
	print "System is under-damped"

# print "omega_Mach0_13 = ", omega_Mach0_13
# print "omega_Mach1 = ", omega_Mach1
print "omega_0 = ", omega_0
print "f_0 = ", f_0
print "k_s = ", k_s
print "c_s = ", c_s

print "G(s) = ", G

'''
# Calculate natural frequency
omega_0 = pow(k_s*N/m_pod,0.5)
print "omega_0 = ", omega_0
print "f_0 = ", f_0
'''

figure('Hyperloop Suspension System - Bode Plot')
bode(G)
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

