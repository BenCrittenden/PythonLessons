#Lesson6_Lists

#Lists can be of numbers or strings

numbers = [5, 6, 7, 8]
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]

#Indicies of lists start from 0! For example

a = numbers[0]
b = numbers[2]

#a would be equal to 5 and b would be equal to 7


#you can append to lists like this:

suitcase = [] 
suitcase.append("sunglasses")
suitcase.append("hat")

#note that this doesn't quite work, it will add both like they're a single item in the list:

suitcase.append(["shirt","shorts"])

"""
indexing of lists is a bit weird.
If you want the first two elements of a list you index them by 0:2,
That looks like it's doing 0, 1, 2, i.e. three, but it actually stops at the last 
number and doesn't do it.
So the first number is where you start and the last number is what you stop BEFORE, 
even if that index doesn't exist here, i.e. 6.
e.g.
"""

suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

# To get sunglasses and hat
first = suitcase[0:2]

# To get passport and laptop
middle = suitcase[2:4]

# To get suit and shoes
last =  suitcase[4:6]

#the short cut to go from the start, or to the end are:
first2 = [:2]
last2 = [4:]

#to find out the index of an item in a list, or place an item in a specific place 
#(moving everything down one)

duck_index = animals.index('duck')
animals.insert(duck_index, 'cobra')

#An example for loop:

for number in my_list:
  print 2 * number

#you can remove items in a list like this:
backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove('dagger')  



#Another example - using append and sort functions too

start_list = [5, 3, 1, 2, 4]
square_list = []

for number in start_list:
  square_list.append(number**2)

square_list.sort()
print square_list

"""
Dictionaries can be thought of as like a phone book where you can look up
a number by using the name. All the entries are paired with a key.
Dictionaries use curly brackets.
Dictionaries are mutable, i.e. you can edit them. (unlike tuples)
"""

new_dict = {} #creates a new, empty dictionary

#Assigning a dictionary with three key-value pairs to `residents`
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number, i.e. 104
print residents['Sloth']
print residents["Burmese Python"]

#You can add to empty dictionaries like this
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair

#But multiple entries like this do not work
menu['Salad','Burger','Fries'] = [10.00, 7.00, 3.00]

#You can delete and reassign entries in dictionaries:

zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}

del zoo_animals['Sloth']
del(zoo_animals['Bengal Tiger']) #alternative way of using del
zoo_animals['Rockhopper Penguin'] = 'Antarctic exhibit'


"""
A bunch of codes that show how to index and manipulate dictionaries.
Note that each key is a single word, but the information that they refer to can be
many different kinds: strings, numbers, lists.
"""

inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# create a new key that indexes a list
inventory['pocket']  = ['seashell','strange berry','lint']

#sort the items in the backpack list 
inventory['backpack'].sort()

#remove dagger from the backpack list
inventory['backpack'].remove('dagger')

#change the value of the gold
inventory['gold'] = inventory['gold'] + 50



"""
Here's a complete programe with for loops, if statemnts, a few functions/methods
and some lists and dictionaries
"""

lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

def average(numbers):
  total = sum(numbers)
  total = float(total)
  average = total / len(numbers)
  
  return average

def get_average(student):
  homework = average(student['homework'])
  quizzes = average(student['quizzes'])
  tests = average(student['tests'])
  
  score = homework*0.1 + quizzes * 0.3 + tests * 0.6
  
  return score
                  
  
def get_letter_grade(score):
  if score >= 90:
    return 'A'
  elif score >= 80:
    return 'B'
  elif score >= 70:
    return 'C'
  elif score >= 60:
    return 'D'
  else:
    return 'F'
  
  
def get_class_average(class_list):
  results = []
  
  for s in class_list:
    results.append(get_average(s))
    
  return average(results)


class_average = get_class_average([lloyd,alice,tyler])

print class_average

print get_letter_grade(class_average)

