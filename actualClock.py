from vpython import *
import time
import numpy as np
clockR=1
clockT=clockR/10

majorTickL=clockR/7
majorTickT=2*np.pi*clockR/400
majorTickW=clockT*1.2

minorTickL=clockR/12
minorTickT=2*np.pi*clockR/600
minorTickW=clockT*1.2

minuteHandL=clockR-majorTickL
minuteHandT=minuteHandL/25
minuteHandOffset=clockT/2+minuteHandT

secondHandL=clockR-majorTickL/2
secondHandT=minuteHandL /50
secondHandOffset=clockT*1.5+minuteHandT

hourHandL=.75*minuteHandL
hourHandT=minuteHandT*1.25
hourHandOffset=clockT+hourHandT

for theta in np.linspace(0,2*np.pi,13):
    majorTik=box(axis=vector(clockR*np.cos(theta),clockR*np.sin(theta),0), color=color.black, length=majorTickL, width=majorTickW, height=majorTickT,pos=vector((clockR-majorTickL/2)*np.cos(theta),(clockR-majorTickL/2)*np.sin(theta),0))
for theta in np.linspace(0,2*np.pi,61):
    minorTik=box(axis=vector(clockR*np.cos(theta),clockR*np.sin(theta),0), color=color.black, length=minorTickL, width=minorTickW, height=minorTickT,pos=vector((clockR-minorTickL/2)*np.cos(theta),(clockR-minorTickL/2)*np.sin(theta),0))
clockFace=cylinder(axis=vector(0,0,1),color=vector(0,1,.8),length=clockT,radius=clockR, pos=vector(0,0,-clockT/2))
hubRadius=clockT/2

hourAngle=np.pi/2
minuteAngle=np.pi/2
minInc=0.0001
hourInc=minInc/12
secondAngle=np.pi/2
secondInc=minInc*60

minuteHand=arrow(axis=vector(0,1,0),color=color.red,shaftwidth=minuteHandT,length=minuteHandL,pos=vector(0,0,minuteHandOffset))
hourHand=arrow(axis=vector(0,1,0),color=color.red,shaftwidth=hourHandT,length=hourHandL,pos=vector(0,0,hourHandOffset))
hub=cylinder(axis=vector(0,0,1),color=color.red,radius=hubRadius,length=2*clockT)
secondHand=arrow(axis=vector(0,1,0),color=color.red,shaftwidth=secondHandT,length=secondHandL,pos=vector(0,0,secondHandOffset))
while True:
    rate(5000)
    hour = time.localtime(time.time())[3]
    if hour>12:
        hour=hour-12
    minute = time.localtime(time.time())[4]
    second = time.localtime(time.time())[5]
    hourAngle=-((hour+minute/60)/12)*2*np.pi+np.pi/2
    minuteAngle=-((minute+second/60)/60)*2*np.pi+np.pi/2
    secondAngle=-(second/60)*2*np.pi+np.pi/2
    
    
    print(second)
    hourHand.axis=vector(hourHandL*np.cos(hourAngle),hourHandL*np.sin(hourAngle),0)
    minuteHand.axis=vector(minuteHandL*np.cos(minuteAngle),minuteHandL*np.sin(minuteAngle),0)
    secondHand.axis=vector(secondHandL*np.cos(secondAngle),secondHandL*np.sin(secondAngle),0)
    