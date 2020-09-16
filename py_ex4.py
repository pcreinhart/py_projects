# This defines how many cars there are 
cars = 100
# This defines how may spaces there are in a car 
space_in_a_car = 4.0
# This defines how many drivers there are
drivers = 30.5
passengers = 90
# This defines how many cars are not being driven 
cars_not_driven = cars - drivers
cars_driven= drivers 
carpool_capacity=cars_driven*space_in_a_car
average_passengers_per_car = passengers/cars_driven

print("There are", cars, "cars available")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "people today")
print("We have",passengers, "to carpool today")
print("We need to put about", average_passengers_per_car, "in each car")
