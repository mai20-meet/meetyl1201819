import turtle
import time
import random
from project import Ball 
from project import PLayer
# score
global score
score=0
global score1
score1=0


turtle.tracer(0,0)
turtle.hideturtle()
turtle.pu()
turtle.goto(200,250)
turtle1=turtle.clone()
turtle1.goto(-250,250)
turtle2=turtle.clone()
turtle2.goto(-300,400)
turtle.write("Ahmad"+str(score),font=("Arial", 16, "normal"))
turtle1.write("uriel"+str(score1),font=("Arial", 16, "normal"))
turtle2.write("AHMAD N URIEL ADVENTURE",font=("Arial", 32, "normal"))
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
screen.setup(1000, 1000)



screen.addshape("A.gif")
MY_BALL=Ball(200,200,50,10,10,"pink")
MY_BALL.shape("A.gif")
ball_alive=True
#player face 
screen=turtle.Screen()
screen.addshape("U4.gif")
Player=PLayer(-250,50,50,15,15,"green")
Player.shape("U4.gif")
player_alive = True

# game sound
from pygame import mixer
mixer.init()
mixer.music.load('song1.mp3')
mixer.music.play()

#defining the ball objects
NUMBER_OF_BALLS=7
MINIMUM_BALL_RADIUS=5
MAXIMUM_BALL_RADIUS=70
MINIMUM_BALL_DX=-2
MAXIMUM_BALL_DX=2
MINIMUM_BALL_DY=-2
MAXIMUM_BALL_DY=2
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
				turtle.goto(200,250)
				print("You have eaten the balls!")    # You should write code to check for the left, top, and bottom edges.
				turtle.write("Ahmad"+str(score),font=("Arial", 16, "normal"))
				# changing bg
				bg=["yellow","pink","light blue","purple","light green"]
				i= random.randint(0,4)
				# screen.addshape(bg[i])
				screen.bgcolor(bg[i])    
	return True		
#check colission between Player and the balls 
def check_Player_collision():
		for ball in BALLS:
			if collide(Player,ball):
				print("shyu")
				R3=Player.r
				R2=ball.r
				if R2 >= R3:
					return False
				else: 
					Player.r+= 1
					Player.shapesize(Player.r/10)
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

					global score1
					score1=score1+1
		
					turtle1.undo()
					
					print("You have eaten the balls!")    # You should write code to check for the left, top, and bottom edges.
					turtle1.write("Uriel"+str(score1),font=("Arial", 16, "normal"))
			
				
		return True		

#def methhod that controlls MY_BALL w the mouse
def movearound(event):
	x=event.x-SCREEN_WIDTH
	y=-event.y+SCREEN_HEIGHT
	MY_BALL.goto(x,y)

turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()


# player movement(keys)
def movearound1(event):
	x=event.x-SCREEN_WIDTH
	y=-event.y+SCREEN_HEIGHT
	player.goto(x,y)
	turtle.listen()

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


step=30
def up():
    Player.dy=step
    Player.dx=0
    Player.move(SCREEN_WIDTH,SCREEN_HEIGHT)
    print("You pressed the up key!")



def down():
    Player.dy=-step
    Player.dx=0
    Player.move(SCREEN_WIDTH,SCREEN_HEIGHT)
    print("You pressed the down key!")

def left():
    Player.dy=0
    Player.dx=-step
    Player.move(SCREEN_WIDTH,SCREEN_HEIGHT)
    print("You pressed the left key!")

def right():
    Player.dx=step
    Player.dy=0
    Player.move(SCREEN_WIDTH,SCREEN_HEIGHT)
    print("You pressed the right key!")


turtle.onkeypress(up, UP_ARROW) 
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)

turtle.listen()
# while function MY_BALL
while RUNNING:
	
	SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2
	SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2	 
	
	move_all_balls(BALLS)
	check_all_balls_collision()

	
	#RUNNING=check_myball_collision() and check_Player_collision()
	if ball_alive:
		ball_alive = check_myball_collision()
	if player_alive:
		player_alive = check_Player_collision()


	if ball_alive==False:
		MY_BALL.clear()
		MY_BALL.ht()


	if player_alive==False:
		Player.clear()
		Player.ht()
	# if(alive1==False and alive2==True):

	# 	#my ball is dead
	# if(alive1==True and alive2==False):
	# 	pass
		#myball is alive, player is dead
	if(ball_alive==False and player_alive==False):
		RUNNING = False
		#both are dead
	
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
		print(SCREEN_WIDTH,SCREEN_HEIGHT)
		turtle.update()
		time.sleep(3)
 







