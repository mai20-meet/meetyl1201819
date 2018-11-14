import turtle
from turtle import Turtle
class Square(Turtle):
	def __init__(self, size, color):
		Turtle.__init__(self)
		self.shapesize= size
		turtle.shape("square")
		turtle.color(color)

t1=Square(10)
t1.random_color()
turtle.mainloop()