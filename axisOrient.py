from vpython import *
import numpy as np
arrowL=2
arrowT=.02
theta=0
bRadius=.05
Xarrow= arrow(axis=vector(1,0,0),color=color.red,length=arrowL,shaftwidth=arrowT)
Yarrow= arrow(axis=vector(0,1,0),color=color.green,length=arrowL,shaftwidth=arrowT)
Zarrow= arrow(axis=vector(0,0,1),color=color.blue,length=arrowL,shaftwidth=arrowT)
pntArrow = arrow(axis=vector(arrowL*np.cos(theta),arrowL*np.sin(theta),0),color=color.orange,length=arrowL,shaftwidth=arrowT)
rotBall = sphere(make_trail=True,trail_color=color.cyan,radius=bRadius,color=color.red,pos=vector(arrowL,0,0))
while True:
    for myAngle in np.linspace(0,2*np.pi,1000):
        rate(150)
        pntArrow.axis=vector(arrowL*np.cos(myAngle),arrowL*np.sin(myAngle),0)
        pntArrow.length=arrowL
        rotBall.pos=vector(arrowL*np.cos(myAngle),arrowL*np.sin(myAngle),0)
        if myAngle == 2*np.pi:
            for myAngle in np.linspace(np.pi/2,2*np.pi,1000):
                rate(150)
                pntArrow.axis=vector(arrowL*np.sin(myAngle),0,arrowL*np.cos(myAngle))
                pntArrow.length=arrowL
                rotBall.pos=vector(arrowL*np.sin(myAngle),0,arrowL*np.cos(myAngle))
                if myAngle == 2*np.pi:     
                    for myAngle in np.linspace(0,2*np.pi,1000):
                        rate(150)
                        pntArrow.axis=vector(0,arrowL*np.sin(myAngle),arrowL*np.cos(myAngle))
                        pntArrow.length=arrowL
                        rotBall.pos=vector(0,arrowL*np.sin(myAngle),arrowL*np.cos(myAngle))
                        if myAngle == 2*np.pi:
                            for myAngle in np.linspace(0,2.5*np.pi,1000):
                                rate(150)
                                pntArrow.axis=vector(arrowL*np.sin(myAngle),0,arrowL*np.cos(myAngle))
                                pntArrow.length=arrowL
                                rotBall.pos=vector(arrowL*np.sin(myAngle),0,arrowL*np.cos(myAngle))
                            


