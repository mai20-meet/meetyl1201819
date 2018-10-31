'''
class Animal(object):
	def __init__(self,sound,name,age,favorite_color,favorite_food):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
		self.favorite_food = favorite_food

	def eat(self,food,favorite_food):

			print("yummy!!" + self.name + " is eating " + food)
	def description(self):
		print(self.name + "is" + str(self.age) +" years old and loves the color "+self.favorite_color)
	def make_sound(self,times):
		print("my sound is " + self.sound*times)
k=Animal("woof","kucha",3,"pink", "pizza")
k.eat("banana","pizza")
print(k.favorite_food)
k.description()
k.make_sound(7)
'''
class person(object):
	def __init__(self,name,age,city,gender):
		self.name=name
		self.age=age
		self.city=city
		self.gender=gender
	def eat(self, food):
		print("my favorite breakfast is " + food)
m=person("mai",15,"london","female","banana")
m.eat ("banana")

	