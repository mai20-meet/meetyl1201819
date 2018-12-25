from turtle import *
import turtle
import random
import math
from random import randint

turtle.colormode(255)

class ball(Turtle):
	def __init__(self,radius,color,speed,dx,dy):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)

		self.dx=dx
		self.dy=dy
	def border(self):
		high=300
		low=-300
		left=-300
		right=300
		if self.xcor() > right or self.xcor()<left or self.ycor()>high or self.ycor() < low:
			self.dx=-self.dx
			self.dy=-self.dy
	def move(self):
		self.goto(self.xcor()+self.dx,self.ycor()+self.dy)
	def random_color(self):

		r = randint(0,255)
		g = randint(0,255)
		b = randint(0,255)
		self.color((r,g,b))
		

turtle.penup()
turtle.pensize(5)
turtle.goto(300,300)
turtle.speed(0)
for i in range (4):
	turtle.pendown()
	turtle.right(90)
	turtle.forward(600)
ball1=ball(10,"pink",5, 13, 10)
ball2=ball(20,"light blue", 5,15, 20)
ball1.penup()
ball2.penup()
ball1.goto(-100,-100)
def check_collision(ball1, ball2):
	x1=ball1.xcor()
	y1=ball1.ycor()
	x2=ball2.xcor()
	y2=ball2.ycor()

	if	math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))<=ball1.radius+ball2.radius:
		print("hi")
		# ball1.goto(random.randint(-300,300),random.randint(-300,300))

		#color1=random.randint(0,225),random.randint(0,225),random.randint(0,225)
		# color2=random.randint(0,225),random.randint(0,225),random.randint(0,225)
		# ball1.color(random.randint(0,225),random.randint(0,225),random.randint(0,225))
		# ball2.color(color2)
		return True 
	else:
		return False

	
while True:

	ball1.move()
	ball2.move() 
	ball1.border()
	ball2.border()

	collied=check_collision(ball1,ball2)
	if collied is True:
		ball1.goto(random.randint(-300,300),random.randint(-300,300))
		ball1.random_color()
		ball2.random_color()


# pygame.mixer.init()
# pygame.mixer.music.load("song.mp3")
# pygame.mixer.music.play(-1)



mainloop()
