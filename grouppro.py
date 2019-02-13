# 
import turtle
pen = turtle.Turtle()
pen.hideturtle()
for i in range(2):
	pen.forward(80)
	pen.left(90)
	pen.forward(30)
	pen.left(90)
pen.penup()
pen.goto(7,6)
pen.write("click me!", font=("Ariel",12,"normal"))
def btnclick(x,y):
	print(x,y)
turtle.onscreenclick(btnclick, 1)
turtle.listen()
turtle.done()