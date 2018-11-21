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

	 


t1=Square(10, "blue")
t1.random_color()
turtle.mainloop()

class Hexagon
	def __init__(self,size)
	self.size = size
	
H=Hexagon(10)