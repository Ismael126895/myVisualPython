from vpython import *
from time import *
mRadius=.5
wallThickness=.1
roomWidth=12
roomDepth=20
roomHeight=15
floor=box(pos=vector(0,-roomHeight/2,0),size=vector(roomWidth,wallThickness,roomDepth), color=color.white)
ceiling=box(pos=vector(0,roomHeight/2,0),size=vector(roomWidth,wallThickness,roomDepth), color=color.white)
backWall=box(pos=vector(0,0,-roomDepth/2),size=vector(roomWidth,roomHeight,wallThickness), color=color.white)
leftWall=box(pos=vector(-roomWidth/2,0,0),size=vector(wallThickness,roomHeight,roomDepth), color=color.white)
rightWall=box(pos=vector(roomWidth/2,0,0),size=vector(wallThickness,roomHeight,roomDepth), color=color.white)
marble=sphere(radius=mRadius,color=color.white)
deltaX=.1
deltaY=.1
deltaZ=.1

xPos=0
yPos=0
zPos=0

run=0
mySpeed=1

def ballColorRed(x):
    marble.color=color.red
button(bind=ballColorRed,text='Red',color=color.black,background=color.red)
def ballColorGreen(x):
    marble.color=color.green
button(bind=ballColorGreen,text='Green',color=color.black,background=color.green)
def ballColorBlue(x):
    marble.color=color.blue
button(bind=ballColorBlue,text='Blue',color=color.black,background=color.blue)
scene.append_to_caption('\n\n')


def runRadio(x):
    print(x.checked)
    global run
    if x.checked == True:
        run=1
    if x.checked == False:
        run=0

radio(bind=runRadio,text='Run')

scene.append_to_caption('\n\n')

def bigBall(x):
    global mRadius
    if x.checked == True:
        mRadius=mRadius*2
        marble.radius=mRadius
    if x.checked== False:
        mRadius=mRadius/2
        marble.radius=mRadius
checkbox(bind=bigBall,text='Big Ball')
scene.append_to_caption('\n\n')
# scene.append_to_caption('   ')
wtext(text='Choose Ball Speed')
scene.append_to_caption('\n\n')
def speed(x):
    global mySpeed
    if x.selected == '1':
        mySpeed=1
    if x.selected == '2':
        mySpeed=2
    if x.selected == '3':
        mySpeed=3
    if x.selected == '4':
        mySpeed=4
    if x.selected == '5':
        mySpeed=6
menu(bind=speed,choices=['1','2','3','4','5'])
scene.append_to_caption('\n\n')
def ballOpacity(x):
    op=x.value
    marble.opacity=op
wtext(text='Choose Ball Opacity')
scene.append_to_caption('\n\n')
slider(bind=ballOpacity,vertical=False,min=0,max=1,value=1,text='Opacity of Ball')
scene.append_to_caption('\n')


while True:
    rate(25)

    xPos=xPos+(deltaX*run*mySpeed)
    yPos=yPos+(deltaY*run*mySpeed)
    zPos=zPos+(deltaZ*run*mySpeed)

    Xrme=xPos+mRadius
    Xlme=xPos-mRadius
    Ytme=yPos+mRadius
    Ybme=yPos-mRadius
    Zbme=zPos-mRadius
    Zfme=zPos+mRadius

    Rwe=roomWidth/2-wallThickness/2
    Lwe=-roomWidth/2+wallThickness/2
    Cwe=roomHeight/2-wallThickness/2
    FLOORwe=-roomHeight/2+wallThickness/2
    Bwe=-roomDepth/2+wallThickness/2
    Fwe=roomDepth/2-wallThickness/2

    if (Xrme>=Rwe or Xlme<=Lwe):
        deltaX=deltaX*(-1)

    if (Ytme>=Cwe or Ybme<=FLOORwe):
        deltaY=deltaY*(-1)

    if (Zfme>=Fwe or Zbme<=Bwe):
        deltaZ=deltaZ*(-1)

    marble.pos=vector(xPos,yPos,zPos)