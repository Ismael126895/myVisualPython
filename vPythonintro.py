from vpython import *
from time import *
floor=box(pos=vector(0,-5,0),color=color.white,length=10,height=.1,width=10)
ceiling=box(pos=vector(0,5,0),color=color.white,length=10,height=.1,width=10)
wall1=box(pos=vector(-5,0,0),color=color.white,length=0.1,height=10,width=10)
wall2=box(pos=vector(5,0,0),color=color.white,length=0.1,height=10,width=10)
wall3=box(pos=vector(0,0,-5),color=color.white,length=10,width=.1,height=10)
ball=sphere(pos=vector(0,0,0),color=color.red,radius=4.9)

while True:
    pass