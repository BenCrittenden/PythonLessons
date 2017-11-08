#Lesson2_methods

#The following are string methods, that work like this:

parrot = "Norwegian Blue"
pi = 3.14

len(parrot) #gives the number of characters, including the white space
str(pi) #converts numbers to strings

#methods that use dot notation only work on strings:

parrot.lower()
parrot.upper()
parrot.isalpha() #checks if all characters are alphabetical

#concatenate strings using +

var = "Hello " + "world"

# the % sign in print acts as an operator
# the letter after the % determines the type of variable to handle e.g. string, floating point number
# you then use a final % symbol to indicate that the print is finished and then...
# you then list the variables in order of appearance


string_1 = "Camelot"
string_2 = "place"
print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

#To get the user to input text into the console, which you then use:

name = raw_input("What is your name? ")
quest = raw_input("What is your quest? ")
color = raw_input("What is your favorite color? ")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)

"""
Here's the fully functional Battleship script. Note a few things:
you need to import the random number generator
the use of 'break' to exit the for loop
the print command at the end that prints the number, doesn't use the % notation


"""

from random import randint

board = []

for x in range(5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

for turn in range(4):

  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

  if guess_row == ship_row and guess_col ==   ship_col:
    print "Congratulations! You sunk my battleship!"
    break
  else:
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
      print "Oops, that's not even in the ocean."
    elif(board[guess_row][guess_col] == "X"):
      print "You guessed that one already."
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
      if turn == 3:
        print 'Game Over'
  
    print "Turn ", turn + 1
    print_board(board)
