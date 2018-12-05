import turtle
from turtle import Turtle
from random import randint
class Square(Turtle):
	def __init__(self, size, color):
		Turtle.__init__(self)
		self.shapesize= size
		turtle.shape("square")
		turtle.colormode(255)
		# turtle.color(color)
		'''
		r = randint(0,255)
		g = randint(0,255)
		b = randint(0,255)
		turtle.color((r,g,b))
		'''		
	def random_color(self):

		r = randint(0,255)
		g = randint(0,255)
		b = randint(0,255)
		self.color((r,g,b))
		self.shape("square")

	 


# t1=Square(10, "blue")
# t1.random_color()

class Hexagon(Turtle):
	def __init__(self,size,color,speed):
		Turtle.__init__(self)
		self.size = size
	
		turtle.begin_poly()
		turtle.fillcolor(color)
		turtle.speed(speed)
		turtle.penup()
		turtle.backward(50)
		turtle.fd(50)
		turtle.right(50)
		turtle.fd(50)
		turtle.rt(50)
		turtle.fd(50)
		turtle.rt(50)
		turtle.fd(50)
		turtle.rt(50)
		turtle.fd(50)
		turtle.rt(50)
		turtle.fd(50)
		turtle.rt(50)
		turtle.fd(50)
		turtle.pendown()
		turtle.end_poly()
		H = turtle.get_poly()
		turtle.register_shape("myFavouriteHexagon", H)
		turtle.shape("myFavouriteHexagon")
H=Hexagon(10, "pink",50)
turtle.mainloop()
# 