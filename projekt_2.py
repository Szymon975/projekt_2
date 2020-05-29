import numpy as np
import scipy
import math

class vector: # wektor euklidesowy dla oddziaływań Słońce-Ziemia-Księżyc
	x = float()
	y = float()

	def __init__(x_arg: float, y_arg: float):
		x, y = x_arg, y_arg

	def lenght():
		return math.hypot(x,y)

	def __add__(self, vec2: vector):
		return vector(self.x + vec2.x, self.y + vec2.y)
	
	def __sub__(self, vec2: vector):
		return vector(self.x - vec2.x, self.y - vec2.y)

	def __iadd__(self, vec2: vector):
		temp = self + vec2
		x = temp.x
		y = temp.y
		return temp
	
	def __isub__(self, vec2: vector):
		temp = self - vec2
		x = temp.x
		y = temp.y
		return temp

	def __mul__(self, multipier: float):
		return vector(self.x * multipier, self.y * multipier)

	def __div__(self, divisor: float):
		return vector(self.x / divisor, self.y / divisor)


class celestial_body: # ciało Słońce/Ziemia/Księżyc
	position = vector()
	velocity = vector()
	acceleration = vector()
	sgp = 0. # standardowy parametr grawitacyjny
	radius = 0.

	def interact(self, cb2: celestial_body):
		vec_to_cb2 = cb2.position - self.position
		distance = (self.position - cb2.position).lenght()
		acceleration += vec_to_cb2 * sgp / distance ** 3

	def update():
		velocity += acceleration
		position += velocity
		acceleration = vector(0.,0.)