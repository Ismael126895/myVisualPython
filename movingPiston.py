from vpython import *
import numpy as np

moving_piston=cylinder(radius=1,length=3,color=color.red,opacity=.5)

while True:
    for myLength in np.linspace(1,6,1000):
        rate(500)
        moving_piston.length=myLength
    for myLength in np.linspace(6,1,1000):
        rate(500)
        moving_piston.length=myLength
