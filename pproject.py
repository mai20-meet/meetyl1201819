import turtle
import time
import random
from project import Ball 
from project import Player
# score
global score
score=0

turtle.tracer(0,0)
turtle.hideturtle()
turtle.pu()
turtle.goto(200,250)
turtle.write(score,font=("Arial", 16, "normal"))
#global verbs
global RUNNING
RUNNING=True
global sleep
SLEEP=0.0077
global SCREEN_WIDTH
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
global SCREEN_HEIGHT
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2
#MY_BALL face
screen=turtle.Screen()
screen.addshape("A.gif")
MY_BALL=Ball(10,10,50,10,10,"pink")
MY_BALL.shape("A.gif")
#player face 
screen=turtle.Screen()
screen.addshape("U4.gif")
Player=Player(15,15,15,15,15,"green")
Player.shape("U4.gif")

# game sound
def play_sound(self,song):
	self.song="song1.mp3"
	os.system("afplay {}&".format("song1.mp3"))

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
	# random balls
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
#defining the method that checks colission between all balls
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
#check colission between MY_BALL and the balls
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
				# score
				global score
				score=score+1
		
				turtle.undo()
				print("You have eaten the balls!")    # You should write code to check for the left, top, and bottom edges.
				turtle.write(score,font=("Arial", 16, "normal"))
					 # if collide(MY_BALL,ball):
				# background = input("pink")
				# if background == "pink":
				#     screen.fill("pink")
				#     pygame.display.update()
	return True		
#check colission between player and the balls 
	def check_myball_collision():
		for ball in BALLS:
			if collide(player,ball):
				print("shyu")
			R3=player.r
			R2=ball.r
			if R2 >= R3:
				return False
			else: 
				player.r+= 1
				player.shapesize(player.r/10)
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
			
				
	return True		

#def methhod that controlls MY_BALL w the mouse
def movearound(event):
	x=event.x-SCREEN_WIDTH
	y=-event.y+SCREEN_HEIGHT
	MY_BALL.goto(x,y)

turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()


# player movement(keys)
def movearound(event):
	x=event.x-SCREEN_WIDTH
	y=-event.y+SCREEN_HEIGHT
	player.goto(x,y)
	turtle.listen

UP_ARROW = "Up" 
LEFT_ARROW = "Left" 
DOWN_ARROW = "Down" 
RIGHT_ARROW = "Right"
TIME_STEP = 100
SPACEBAR = "space" 

UP = 0
LEFT=1
DOWN=2
RIGHT=3

UP_EDGE = 400
DOWN_EDGE = -400
RIGHT_EDGE = 300
LEFT_EDGE = -300


direction = UP

def up():
    global direction 
    direction=UP

    print("You pressed the up key!")


def down():
    global direction 
    direction=DOWN 
    print("You pressed the down key!")

def left():
    global direction 
    direction=LEFT 
    print("You pressed the left key!")

def right():
    global direction 
    direction=RIGHT 
    print("You pressed the right key!")

def movearound(event):
	x=event.x-SCREEN_WIDTH
	y=-event.y+SCREEN_HEIGHT
	player.goto(x,y)

turtle.onkeypress(up, UP_ARROW) 
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)

turtle.listen()
# while function
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
		#game over
		you_lost.penup()
		image = "over.gif"
		turtle.register_shape(image)
		you_lost.shape(image)
		you_lost.showturtle()
		
		turtle.update()
		
		time.sleep(3)






