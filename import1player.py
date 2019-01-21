import turtle
#creat a class
class Ball(turtle.Turtle):
	def __init__(self,x,y,r,dx,dy,color):
		
		turtle.Turtle.__init__(self)
#defining the objects in the class
		self.penup()
		self.goto(x,y)
		self.x=x
		self.y=y
		self.r=r
		self.dx=dx
		self.dy=dy
		self.color(color)
		self.shape("circle")
		self.shapesize(r/10)
#defining move function
	def move(self, screen_width,screen_height):
#defining the objects in the method
		current_x=self.xcor()
		new_x=current_x+self.dx
		current_y=self.ycor()
		new_y=current_y+self.dy
		right_side_ball=new_x+self.r
		left_side_ball=new_x-self.r
		up_side_ball=new_y+self.r
		down_side_balL=new_y-self.r
		
		self.goto(new_x,new_y)
#if- mouse controlling
		if right_side_ball>=screen_width:
			self.dx=-self.dx
		if left_side_ball<=-screen_width:
			self.dx=-self.dx
		if up_side_ball>=screen_height:
			self.dy=-self.dy
		if down_side_balL<=-screen_height:
			self.dy=-self.dy	


	

