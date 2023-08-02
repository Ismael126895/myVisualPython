from vpython import *
import numpy as np

glassBulb1 = sphere(radius = 1.25, color=color.white, opacity=.3)
glassCyl1 = cylinder(radius=.65, length=6,color = color.white, opacity=.3)
mercSphere1 = sphere(radius=1, color=color.red)
mercColumn1 = cylinder(radius=.45,length=6, color=color.red)
mercColumn1Length=1
mercColumn1LengthDelta=.01

glassBulb2 = sphere(pos = vector(0,10,0),radius = 1.25, color=color.white, opacity=.3)
glassCyl2 = cylinder(pos = vector(0,10,0),radius=.65, length=6,color = color.white, opacity=.3)
mercSphere2 = sphere(pos = vector(0,10,0),radius=1, color=color.red)
mercColumn2 = cylinder(pos = vector(0,10,0),radius=.45,length=6, color=color.red)
mercColumn2Length=1
mercColumn2LengthDelta=0.02

for tick1 in np.linspace(1,6,15):
    box(size=vector(.05,.5,.25), color=color.white,pos=vector(tick1,0,.5))
    box(size=vector(.05,.5,.25), color=color.white,pos=vector(tick1,10,.5))


while True:
    rate(50)
    mercColumn1Length=mercColumn1Length+mercColumn1LengthDelta
    mercColumn2Length=mercColumn2Length+mercColumn2LengthDelta
    mercColumn1.length=mercColumn1Length
    mercColumn2.length=mercColumn2Length
    if mercColumn1Length>=6 or mercColumn1Length<=.1:
        mercColumn1LengthDelta=mercColumn1LengthDelta*(-1)
    if mercColumn2Length>=6 or mercColumn2Length<=.1:
        mercColumn2LengthDelta=mercColumn2LengthDelta*(-1)

    
        