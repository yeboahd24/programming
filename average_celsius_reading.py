#!usr/bin/env/python3

# Averge Celsius Reading
# NB: in this example we are give only the fahrenheit so we have to find the celsius

def average_celsius(fahrenheit_readings):
	# Collect Celsius numbers here:
	celsius_numbers = []
	for fahrenheit in fahrenheit_readings:
		celsius_conversion = (fahrenheit - 32)/1.8
		celsius_numbers.append(celsius_conversion)

	# Get sum of all Celsius numbers:
	sum_ = 0.0
	for celsius in celsius_numbers:
		sum_+=celsius
	return sum_ / len(celsius_numbers)


#Test Case
data = [15.6, 9.6, 45.09]
print(average_celsius(data))


