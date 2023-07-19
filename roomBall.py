from vpython import *
from time import *
floor=box(pos=vector(0,-5,0),size=vector(10,.1,10),color=color.white)
ceiling=box(pos=vector(0,5,0),size=vector(10,.1,10),color=color.white)
wall1=box(pos=vector(-5,0,0),size=vector(0.1,10,10),color=color.white)
wall2=box(pos=vector(5,0,0),size=vector(0.1,10,10),color=color.white)
wall3=box(pos=vector(0,0,-5),size=vector(10,10,0.10),color=color.white)
ball=sphere(pos=vector(0,0,0),color=color.red,radius=.75)
deltaX=.1
xPos=0
while True:
    rate(10)
    xPos=xPos+deltaX
    if (xPos>5 or xPos<-5):
        deltaX=deltaX*(-1)
    ball.pos=vector(xPos,0,0)
    pass