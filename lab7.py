from turtle import *
import random
import math
class ball(Turtle):
	def __init__(self,radius,color,speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)

ball1=ball(10,"pink",50)
ball2=ball(20,"light blue", 50)
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
		ball1.goto(100,100)
	else : 
		print("yay")
check_collision(ball1,ball2)


mainloop()