from vpython import *
import numpy as np

thermometer_tube=cylinder(pos=vector(0,0,0),radius=.4,length=5,color=color.red,opacity=1)
thermometer_bulb=sphere(pos=vector(0,0,0),radius=.8, color=color.red,opacity=1)

while True:
    for tube_length in np.linspace(1,3,1000):
        rate(500)
        thermometer_tube.length=tube_length
    for tube_length in np.linspace(3,1,1000):
        rate(500)
        thermometer_tube.length=tube_length