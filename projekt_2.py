import numpy as np
import scipy
import math

number_of_asteroids = 1000

class vector: # wektor euklidesowy dla oddziaływań Słońce-Ziemia-Księżyc
	x = float()
	y = float()

	def __init__(x_arg: float, y_arg: float):
		x, y = x_arg, y_arg

	def __init__():
		x, y = 0, 0

	def lenght():
		return math.hypot(x,y)

	def __add__(self, vec2):
		return vector(self.x + vec2.x, self.y + vec2.y)
	
	def __sub__(self, vec2):
		return vector(self.x - vec2.x, self.y - vec2.y)

	def __iadd__(self, vec2):
		temp = self + vec2
		x = temp.x
		y = temp.y
		return temp
	
	def __isub__(self, vec2):
		temp = self - vec2
		x = temp.x
		y = temp.y
		return temp

	def __mul__(self, multipier: float):
		return vector(self.x * multipier, self.y * multipier)

	def __div__(self, divisor: float):
		return vector(self.x / divisor, self.y / divisor)


class celestial_body: # ciało Słońce/Ziemia/Księżyc
	position : vector
	velocity : vector
	acceleration : vector
	sgp = 0. # standardowy parametr grawitacyjny
	radius = 0.

	def interact(self, cb2):
		vec_to_cb2 = cb2.position - self.position
		distance = (self.position - cb2.position).lenght()
		acceleration += vec_to_cb2 * sgp / distance ** 3

	def update():
		velocity += acceleration
		position += velocity
		acceleration = vector(0.,0.)



class simualtion:
	asteroid_x = np.zeros(shape=(number_of_asteroids)) # numpy array'e asteroidów wrzuci się do oddzielnej klasy
	asteroid_y = np.zeros(shape=(number_of_asteroids))
	asteroid_velocity_x = np.zeros(shape=(number_of_asteroids))
	asteroid_velocity_y = np.zeros(shape=(number_of_asteroids))
	asteroid_acceleration_x = np.zeros(shape=(number_of_asteroids))
	asteroid_acceleration_y = np.zeros(shape=(number_of_asteroids))
	Earth : celestial_body
	Sun : celestial_body
	Moon : celestial_body
	collision_angles = []
	asteroid_collision_mask = np.ones(shape=(number_of_asteroids)) # maska do oznaczania, czy asteroida uderzyła w ciało

	def __init__():
		# tu będzie implementacja rozmieszczania ciał niebieskich i asteroid
		return

	def simulate(): # główna metoda symulacji
		while True: #warunek przzerwania symulacji zostanie dodany potem
			#interakcje grawitacyjne ciał
			Earth.interact(Sun)
			Earth.interact(Moon)
			Sun.interact(Earth) # można by przykleić Słońce w punkcie (0,0), do rozważenia
			Sun.interact(Moon)
			Moon.interact(Earth)
			Moon.interact(Sun)
			for body in [Sun, Earth, Moon]:
				asteroid_vec_to_body_x = numpy.full((number_of_asteroids), body.position.x) - asteroid_x
				asteroid_vec_to_body_y = numpy.full((number_of_asteroids), body.position.y) - asteroid_y
				asteroid_distance = np.hypot(asteroid_vec_to_body_x, asteroid_vec_to_body_y)
				asteroid_acceleration_x += asteroid_vec_to_body_x * body.sgp / asteroid_distance ** 3
				asteroid_acceleration_y += asteroid_vec_to_body_y * body.sgp / asteroid_distance ** 3
			#aktualizacje pozycji
			Earth.update()
			Moon.update()
			Sun.update()
			asteroid_velocity_x += asteroid_acceleration_x
			asteroid_velocity_y += asteroid_acceleration_y
			asteroid_x += asteroid_velocity_x
			asteroid_y += asteroid_velocity_y
			asteroid_acceleration_x = np.zeros(shape=(number_of_asteroids)) #czyszczenie przypieszeń po kroku
			asteroid_acceleration_y = np.zeros(shape=(number_of_asteroids))
			#kolizje ogarnie się potem
		
		
