import turtle
import time
import random
from project import Ball 
turtle.tracer(0,0)
turtle.hideturtle()
running=True
sleep=0.0077
#WRITE BIG LETTERS
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2
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
	color=((random.random(), random.random(), random.random()))
	MY_BALL2=Ball(x,y,r,dx,dy,color)
	BALLS.append(MY_BALL2)
def move_all_balls(BALLS):
	for ball in BALLS: 
		ball.move(screen_width,screen_height)
def collide(ball_a,ball_b):
	if ball_a==ball_b:
		return False
	x1=ball_a.xcor()
	x2=ball_b.xcor()
	y1=ball_a.ycor()
	y2=ball_b.ycor()
	d=((x1-x2)**2+(y1-y2)**2)**0.5
	if d+10 <= ball_a.r+ball_b.r:
		return True
	else:
		return False
def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_a,ball_b):
				r1=ball_a.r
				r2=ball_b.r 
				r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
				dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				dy=random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
				x=random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
				y=random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				color=((random.random(), random.random(), random.random()))
				if r1 >= r2:
					ball_a.r+= 1
					ball_a.shapesize(r/10)
					ball_b.r=r
					ball_b.shapesize(r/10)
					ball_b.penup()
					ball_b.goto(x,y)
					ball_b.x=x
					ball_b.y=y
					ball_b.dx=dx
					ball_b.dy=dy
					ball_b.color(color)
					ball_b.shape("circle")
				else:
					ball_b.r+= 1
					ball_b.shapesize(r/10)
					ball_a.r=r
					ball_a.shapesize(r/10)
					ball_a.penup()
					ball_a.goto(x,y)
					ball_a.x=x
					ball_a.y=y
					ball_a.dx=dx
					ball_a.dy=dy
					ball_a.color(color)
					ball_a.shape("circle")
def check_myball_collision():
	for ball in BALLS:
		if collide(MY_BALL,ball):
			R1=MY_BALL.r
			R2=ball.r
			if R2 >= R1:
				return False
			else: 
				MY_BALL.r+= 1
				MY_BALL.shapesize(r/10)
				ball_b.r+= 1
				ball.shapesize(r/10)
				ball.r=r
				ball.shapesize(r/10)
				ball.penup()
				ball.goto(x,y)
				ball.x=x
				ball.y=y
				ball.dx=dx
				ball.dy=dy
				ball.color(color)
				ball.shape("circle")





					





