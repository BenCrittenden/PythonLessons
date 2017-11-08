#Lesson5_FunctionsAndModules

#to use functions from a given module / library:
#sqrt is a function in the math library, it does not exist in basic python

import math
answer = math.sqrt(25)

#but if I don't want to write math. infront of sqrt every time I use it:

from math import sqrt
answer = sqrt(25)

#and if I want to import all the functions from a module so that I can simply call
#them without pointing to the module, use the * wildcard:

from math imort *
answer = sqrt(25)

#to find out what type a variable is:

type('what')

#A function with an if statement, where the if statement uses an or
#note that for the or, you need to wrtie type(arg1) twice
#type(arg1) == int or float    doesn't work
#also note that return is used to say what the function spits out

def distance_from_zero(arg1):
  if type(arg1) == int or type(arg1)==float:
  	return abs(arg1)
  else:
    return 'Nope'

#Here's an example of a bunch of functions that calcuate the cost of a holiday:

def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == 'Charlotte':
    price = 183
  elif city == 'Tampa':
    price = 220
  elif city == 'Pittsburgh':
    price = 222
  elif city == 'Los Angeles':
    price = 475
    
  return price

def rental_car_cost(days):
  if days >= 7:
    cost = (days * 40) - 50
  elif days >= 3:
    cost = (days * 40) - 20
  else:
    cost = days * 40
        
  return cost

def trip_cost(city,days,spending_money):
  cost = hotel_cost(days)
  cost = cost + rental_car_cost(days)
  cost = cost + plane_ride_cost(city)
  cost = cost + spending_money
  
  return cost

price = plane_ride_cost('Los Angeles')
cost = rental_car_cost(5)
total = trip_cost('Los Angeles',5,600)

print price
print cost
print total


