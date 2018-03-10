class Animal(object):
	is_alive = True
	def __init__(self, name, age, is_hungry):
		self.name = name
		self.age = age
		self.is_hungry = is_hungry
	def description(self):
		print(self.name, self.age, self.is_hungry)

zebra = Animal('zebra', 5, True)
zebra.description()