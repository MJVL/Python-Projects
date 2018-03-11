class Triangle(object):
	number_of_sides = 3
	def __init__(self, angle1, angle2, angle3):
		self.angle1 = angle1
		self.angle2 = angle2
		self.angle3 = angle3
	def check_angles(self):
		return self.angle1 + self.angle2 + self.angle3 == 180

class Equilateral(Triangle):
	angle = 60
	def __init__(self):
		self.angle1 = self.angle2 = self.angle3 = self.angle



my_triangle = Triangle(45, 45, 90)
print("# of Sides: %d, Is Triangle: %s" % (my_triangle.number_of_sides, my_triangle.check_angles()))


class Car(object):
	condition = "new"
	def __init__(self, model, color, mpg):
		self.model = model
		self.color = color
		self.mpg = mpg
	def display_car(self):
		return "This is a %s %s with %d MPG." % (self.color, self.model, self.mpg)
	def drive_car(self):
		self.condition = "used"

class ElectricCar(Car):
	def __init__(self, model, color, mpg, battery_type):
		super(ElectricCar, self).__init__(model, color, mpg)
		self.battery_type = battery_type
	def drive_car(self):
		self.condition = "like new"

my_car = Car("Civic", "Blue", 22)
print(my_car.display_car())


class Point3D(object):
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	def __repr__(self):
		return "(%d, %d, %d)" % (self.x, self.y, self.z)

my_point = Point3D(1,2,3)
print(my_point)