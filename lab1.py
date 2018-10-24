import turtle
print("mai")
print("mai"*3)
print("mai"*100)
number1=6
print(number1)
number2=number1/2
print(number2)
a=[1,2,3] 
for i in a:
	print (i)

for banana in a:
	print (banana)
	print(banana*2)

b = sum(a)
print (b)	
turtle.penup()
turtle.goto(100,100)
turtle.penup()
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.pendown()
turtle.circle(100)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.circle(120)
turtle.penup()
turtle.goto(-50,50)
turtle.pendown()
turtle.circle(100)
turtle.mainloop()