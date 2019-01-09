import turtle
import time
import random
from project import Ball 
turtle.tracer(0,0)
turtle.hideturtle()
running=True
sleep=0.0077
screen_width=turtle.getcanvas().winfo_width()/2
screen_height=turtle.getcanvas().winfo_height()/2
MY_BALL=Ball(10,10,10,10,10,"pink")
NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=100
MINIMUM_BALL_DX=-5
MAXIMUM_BALL_DX=5
MINIMUM_BALL_DY=-5
MAXIMUM_BALL_DY=5
BALLS=[]
for i in range(NUMBER_OF_BALLS):
	r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	dy=random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
	x=random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y=random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	color=random.randint((random.random(), random.random(), random.random()))
	MY_BALL2=Ball(x,y,r,dx,dy,color)
	BALLS.append(MY_BALL2)