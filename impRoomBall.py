from vpython import *
from time import *

bRadius=3
rThickness=1
rWidth=10
rDepth=15
rHeight=10

floor=box(pos=vector(0,-rHeight/2,0),size=vector(rWidth,rThickness,rDepth),color=color.white)
ceiling=box(pos=vector(0,rHeight/2,0),size=vector(rWidth,rThickness,rDepth),color=color.white)
wall1=box(pos=vector(-rWidth/2,0,0),size=vector(rThickness,rHeight,rDepth),color=color.white)
wall2=box(pos=vector(rWidth/2,0,0),size=vector(rThickness,rHeight,rDepth),color=color.white)
back=box(pos=vector(0,0,-rDepth/2),size=vector(rWidth,rHeight,rThickness),color=color.white)
ball=sphere(pos=vector(0,0,0),color=color.red,radius=bRadius)
deltaX=.1
xPos=0

while True:
    rate(20)
    xPos=xPos+deltaX
    xRBE=xPos+bRadius
    xLBE=xPos-bRadius
    Rwe=rWidth/2-rThickness/2
    Lwe=-rWidth/2+rThickness/2
    if (xRBE>=Rwe or xLBE<Lwe):
        deltaX=deltaX*(-1)
    ball.pos=vector(xPos,0,0)
    pass