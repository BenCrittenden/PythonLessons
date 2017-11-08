#Lesson9_Loops

#Here's the basic form of a while loop

loop_condition = True

while loop_condition:
  print "I am a loop"
  loop_condition = False


#and another with a not equal and or statement

while choice != "y" and choice != "n":  # Fill in the condition (before the colon)
  choice = raw_input("Sorry, I didn't catch that. Enter again: ")

#Here's a loop that uses the shorter += to self-update the value of a variable.
#It also uses an if statement to terminate, rather than make the loop terminate due to
#the term being evaluated by the loop statement becoming false

count = 0

while True:
  print count
  count += 1
  if count >= 10:
    break

 # You can use else statements in while loops to give an output once the while terminates

from random import randint
random_number = randint(1, 10)
guesses_left = 3

 while guesses_left > 0:
  
  guesses_left -= 1
  
  guess = (int(raw_input("Your guess: ")))
  if guess == random_number:
    print 'You win!'
    break
    
else:
  print 'You lose.'



#You can use a for loop to loop through the characters in a string

word = "eggs!"

for w in word:
  print w

#if you want to print a bunch of statements, that accrue incrementally, but print all
#at once then you do: add a comma after each print statement and simply call print when
#you finally want to print them all.
#This also resuls in printing on a single line.

for char in phrase:
  char = char.lower()
  if char == 'a':
    print "X",
  else:
    print char,

print  


#When looping through dictionaries, you loop through the keys, not the values.
#You can then use the keys to get the values

d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
  print key,
  print " ",
  print d[key],
  
print



#if you're looping over, say a dictionary, and you want to keep track of how many
#iterations you've done, use 'index ___ in enumerate(var)' to do this.
#this will give you an idex number to indicate iteration number
#here I use index + 1 as idex counts from 0, a la python, which looks a bit weird.

choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
  print index + 1, item



#If you want to comapre two lists, you can put them both into a for loop using zip:
#This will give you both values and terminate at the end of the shorter loop.
#also works for more than 2

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
  print max(a,b)




#you can add else statements to for loops too.
#these will only execute if the for loop terminates properly, otherwise it is ignored

fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
  if f == 'tomato':
    print 'A tomato is not a fruit!' # (It actually is.)
    break
  print 'A', f
else:
  print 'A fine selection of fruits!'


