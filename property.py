class Temperature:
	'''This a class without property
	therfore instance method will be
	call with ()'''
	def __init__(self, celsius, fahrenheit):
		self.celsius=celsius
		self.fahrenheit=fahrenheit

	def fahrenheit_test(self):
		return self.fahrenheit*9/5+32

temp = Temperature(5,10)
print(temp.fahrenheit_test())


class PropertyTemperature:
	def __init__(self, celsius):
		self.celsius=celsius

	@property
	def test_celsius(self):
		return self.celsius*9/5+32

ptemp=PropertyTemperature(5)
print(ptemp.test_celsius)

