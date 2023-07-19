from vpython import *
from time import *

bRadius=.75
rThickness=1
rWidth=10
rDepth=15
rHeight=10

floor=box(pos=vector(0,-rHeight/2,0),size=vector(rWidth,rThickness,rDepth),color=color.white)
ceiling=box(pos=vector(0,rHeight/2,0),size=vector(rWidth,rThickness,rDepth),color=color.white)
wall1=box(pos=vector(-rWidth/2,0,0),size=vector(rThickness,rHeight,rDepth),color=color.white)
wall2=box(pos=vector(rWidth/2,0,0),size=vector(rThickness,rHeight,rDepth),color=color.white)
wall3=box(pos=vector(0,0,-rDepth/2),size=vector(rWidth,rHeight,rThickness),color=color.white)
ball=sphere(pos=vector(0,0,0),color=color.red,radius=bRadius)
deltaX=.1
xPos=0
bounceWidth=bRadius+rThickness
while True:
    rate(50)
    xPos=xPos+deltaX
    if (xPos>((rWidth)/2-bounceWidth) or xPos<=-((rWidth)/2-bounceWidth)):
        deltaX=deltaX*(-1)
    ball.pos=vector(xPos,0,0)
    pass