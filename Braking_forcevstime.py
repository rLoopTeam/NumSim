import matplotlib.pyplot as plt
import numpy as np
import csv

def graph():
    time, force_x, force_y = np.loadtxt(open("1.csv", "rb"), delimiter = ',', skiprows = 1, unpack = True)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(time, force_y, label = 'Force in Y-direction')
    ax.plot(time, force_x, label = 'Force in X-direction')
    ax.legend()
    plt.title('Braking Force')
    plt.xlabel('Time in ms')
    plt.ylabel('Force in N')
    plt.grid(True)
    plt.show()

graph()
