from vpython import *
import numpy as np
mySphere=sphere(radius=1,color=vector(1,0,0))
while True:
    rate(1)
    for par1 in np.linspace(0,1,100):
        for par2 in np.linspace(0,1,100):
            for par3 in np.linspace(0,1,100):
                mySphere.color=vector(par1,par2,par3)
