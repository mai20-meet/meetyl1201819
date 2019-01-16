import turtle
import time
import random
from project import Ball 
global score
score=0
turtle.tracer(0,0)
turtle.hideturtle()
turtle.pu()
turtle.goto(200,250)
turtle.write(score,font=("Arial", 16, "normal"))
#global varbs
global RUNNING
RUNNING=True
global sleep
SLEEP=0.0077
global SCREEN_WIDTH
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
global SCREEN_HEIGHT
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2

#creating my player
MY_BALL=Ball(10,10,50,10,10,"pink")
#defining the ball objects
NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=100
MINIMUM_BALL_DX=-5
MAXIMUM_BALL_DX=5
MINIMUM_BALL_DY=-5
MAXIMUM_BALL_DY=5
BALLS=[]
#def-list
for i in range(NUMBER_OF_BALLS):
	r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	dy=random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
	x=random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y=random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	color=((random.random(), random.random(), random.random()))
	
	MY_BALL2=Ball(x,y,r,dx,dy,color)
	BALLS.append(MY_BALL2)
#defining the method that moves the balls
def move_all_balls(BALLS):
	for ball in BALLS: 
		ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)
#defining the method that check colission between 2 balls 
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
##defining the method that check colission between all balls
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
					if ball_a.r < MAXIMUM_BALL_RADIUS:
						ball_a.r+= 1
					ball_a.shapesize(ball_a.r/10)
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
					if ball_b.r < MAXIMUM_BALL_RADIUS:
						ball_b.r+= 1
					ball_b.shapesize(ball_b.r/10)
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
#that check colission between the player and the balls
def check_myball_collision():
	for ball in BALLS:
		if collide(MY_BALL,ball):
			print("collide")
			R1=MY_BALL.r
			R2=ball.r
			if R2 >= R1:
				return False
			else: 
				MY_BALL.r+= 1
				MY_BALL.shapesize(MY_BALL.r/10)
				r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
				dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				dy=random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
				x=random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
				y=random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				color=((random.random(), random.random(), random.random()))
			
				ball.shapesize(r/10)
				ball.r=r
				ball.penup()
				ball.goto(x,y)
				ball.x=x
				ball.y=y
				ball.dx=dx
				ball.dy=dy
				ball.color(color)
				ball.shape("circle")
				global score
				score=score+1
		
				turtle.undo()
				print("You have eaten the balls!")    # You should write code to check for the left, top, and bottom edges.
				turtle.write(score,font=("Arial", 16, "normal"))
	return True			
#def methhod that controlls the player w the mouse
def movearound(event):
	x=event.x-SCREEN_WIDTH
	y=-event.y+SCREEN_HEIGHT
	MY_BALL.goto(x,y)

turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()

while RUNNING:
	
	SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2
	SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2	 
	
	move_all_balls(BALLS)
	check_all_balls_collision()
	
	RUNNING=check_myball_collision()
	
	turtle.update()
	time.sleep(SLEEP)
	if RUNNING==False:
		you_lost =turtle.Turtle() 
		#you_lost.hideturtle()
		you_lost.penup()
		image = "over.gif"
		turtle.register_shape(image)
		you_lost.shape(image)
		you_lost.showturtle()
		
		turtle.update()
		
		time.sleep(3)






