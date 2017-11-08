#Lesson13_Classes

"""
Classes are a feature of object oriented programming
A class is a grouping of data and functions (methods).
An object is something in python that has some data and methods associated with it
A class is basically a blueprint for a object. And an object is an instance of a class


Just as def is used to define a function,
class is used to define a class
"""

#Define a class called animal, that inherits object properties.
#In the body of the class enter 'pass'. This doesn't do anything, but acts as a placeholder
#as python expects something to go there
class Animal(object):
  #Description
  pass


#the first thing you need to do when setting up a new class is to initialise the 
#object that you're creating.
#You initialize with self by convention (it's not required, but it's what everyone does)

class Animal(object):
  #Description
  def __init__(self):
    pass

#Give a second argument to the initialisation so that the object gets a name
class Animal(object):
  #Description
  def __init__(self,name):
    self.name = name


 #Creating a class - note the dot notation

 class Animal(object):
  #Description
  def __init__(self,name):
    self.name = name
    
zebra = Animal("Jeffrey")
print zebra.name


#An example with a few extra attributes
class Animal(object):
  """Makes cute animals."""

  def __init__(self, name, age, is_hungry):
    self.name = name
    self.age = age
    self.is_hungry = is_hungry


zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)


#If you want all the objects to have a certain attribute by default:
#put the attribute outside of the __init__() 
#now for example zebra.alive would give you True

class Animal(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age

#As well as giving objects names etc, you can also give them methods, defined in
#the usual way, most likely using self as one of the arguments

#create a method (description) in animal that prints the name and age of the animal
#Here it also has a member variable, is_alive, which all Animals will inherit, with
#the default value of True

class Animal(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def description(self):
    print self.name
    print self.age
    
hippo = Animal("Mary",23)

hippo.description()
#you can also get the same info by doing:
print hippo.name, hippo.age


"""
Inhertance:
If you have a 'bear' class and you create a 'panda' class you could have the panda 
class inherit all of the attributes of the bear class.

The way that one class inherits another is by passing the name of the 'mother' class
as an argument in the definition. In the example below, we pass object for the Shape
class (i.e. no inheritance, or at least the most general kind), but then we pass Shape
as the argument when creating the Triangle class.
"""
class Shape(object):
  """Makes shapes!"""
  def __init__(self, number_of_sides):
    self.number_of_sides = number_of_sides

class Triangle(Shape):
  def __init__(self,side1,side2,side3):
    self.side1 = side1
    self.side2 = side2
    self.side3 = side3


"""
Let's say that you've created an employee class, and you can calculate their wages
using the .calculate_wage method.
You then create a part-time employee class which inherits the employee class.
You're happy with most of the attributes / methods, but the .calculate_wage needs
to be changed as the part timers are paid less for the same number of hours. If you
re-define this method it will overwrite the one that it inherited.

Note that because PartTimeEmployee inherits the __init__() I don't need to define that
again
"""

class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

class PartTimeEmployee(Employee):
  
  def calculate_wage(self,hours):
    self.hours = hours
    return hours * 12.00


"""
Now say that you want the option of still being able to see the result of calculate_wage
from the parent's class.

In the derived/child class define a new function.
use the super function to tell it which child level it is going to and the method that
you want to use, here that's calculate wage. Don't forget to give calculate wage the
argument that it needs.

"""

class PartTimeEmployee(Employee):

  def full_time_wage(self,hours):
    return super(PartTimeEmployee,self).calculate_wage(hours)
  
milton = PartTimeEmployee('Milton')
print milton.full_time_wage(10)



#A final example from the lesson.
#Here we change the __init__ of the child, but it will still inherit the same
#check_angles method of Triangle.
#Equilateral also has a member variable, since by definition all angles = 60deg

class Triangle(object):
  
  number_of_sides = 3
  def __init__(self,angle1,angle2,angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3
    
  def check_angles(self):
    if (self.angle1 + self.angle2 + self.angle3 == 180):
      return True
      print 'True'
    else:
      return False
      print 'False'
      
class Equilateral(Triangle):
  
  angle = 60
  def __init__(self):
    self.angle1 = self.angle
    self.angle2 = self.angle
    self.angle3 = self.angle
    


my_triangle = Triangle(90,30,60)
print my_triangle.number_of_sides
print my_triangle.check_angles()


#An example of a class and how to reference variables within the class within functions
#contained in that class

class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
    
  def display_car(self):
    message = 'This is a ' + self.color + ' ' + self.model + ' with ' + str(self.mpg) + ' MPG.' 
    print message

  def drive_car(self):
    self.condition = 'used'

my_car = Car("DeLorean", "silver", 88)

my_car.display_car()

print my_car.condition #prints new
my_car.drive_car()
print my_car.condition #prints used

#let's say that I want to make a child class of car called electric car,
#that can be done like this:
#note that it still requires my to define model, color, mpg - these aren't automatically
#inherited. 
#There's also a new drive_car method for ElectricCar, which overwrites Car's method 
#with the same name.

class ElectricCar(Car):
  
  def __init__(self, battery_type, model, color, mpg):
    self.battery_type = battery_type
    self.model = model
    self.color = color
    self.mpg   = mpg
    
  def drive_car(self):
    self.condition = 'like new'


"""
In python, classes can have a __repr__() method (representation)

The purpose of these, as far as I can tell is to act somewhat like a description
of what that class holds. For good practice, the output should be a string that 
you can directly represent in python, such as a variable or list.

Note that the only input to __repr__ is self.

A related method is __str__()

"""

class Point3D(object):
  
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
    
  def __repr__(self):
    return "(%d, %d, %d)" % (self.x, self.y, self.z)
  
my_point = Point3D(1,2,3)

print my_point

