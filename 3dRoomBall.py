from vpython import *
from time import *

bRadius=.5
rThickness=0.1
rWidth=12
rDepth=20
rHeight=2

floor=box(pos=vector(0,-rHeight/2,0),size=vector(rWidth,rThickness,rDepth),color=color.white)
ceiling=box(pos=vector(0,rHeight/2,0),size=vector(rWidth,rThickness,rDepth),color=color.white)
wall1=box(pos=vector(-rWidth/2,0,0),size=vector(rThickness,rHeight,rDepth),color=color.white)
wall2=box(pos=vector(rWidth/2,0,0),size=vector(rThickness,rHeight,rDepth),color=color.white)
back=box(pos=vector(0,0,-rDepth/2),size=vector(rWidth,rHeight,rThickness),color=color.white)
ball=sphere(pos=vector(0,0,0),color=color.red,radius=bRadius)

deltaX=.1
deltaY=.1
deltaZ=.1

xPos=0
yPos=0
zPos=0

while True:
    rate(140)
    xPos=xPos+deltaX
    yPos=yPos+deltaY
    zPos=zPos+deltaZ

    xRBE=xPos+bRadius
    xLBE=xPos-bRadius

    yTBE=yPos+bRadius
    yBBE=yPos-bRadius

    zFBE=zPos+bRadius
    zBBE=zPos-bRadius

    Rwe=rWidth/2-rThickness/2
    Lwe=-rWidth/2+rThickness/2

    Cwe=rHeight/2-rThickness/2
    Fwe=-rHeight/2+rThickness/2

    Bwe=-rDepth/2+rThickness/2
    Frwe=rDepth/2-rThickness/2
    if (xRBE>=Rwe or xLBE<=Lwe):
        deltaX=deltaX*(-1)
    if (yTBE>=Cwe or yBBE<=Fwe):
        deltaY=deltaY*(-1)
    if (zFBE>=Frwe or zBBE<=Bwe):
        deltaZ=deltaZ*(-1)
    ball.pos=vector(xPos,yPos,zPos)
    