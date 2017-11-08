#Lesson8_Battleships

#I need to start thinking of matrices as lists of lists
#For example a 5 x 5 matrix could be thought of as both a square and as a list
#with 5 points, where each of the five points has a list of 5 values.

board = []

for r in range(5):
  board.append(["O"] * 5)

print board 

"""
prints:
[['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], 
['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]
""" 

#to print the board, one row at a time, to give the impression that it's a matrix
#you can do the following.
#the " ".join() method removes the quotes and square brackets surrounding the string
#and puts an empty space between the letters. There could be any string that you wanted 
#here.
#Not also that in python 0:5 doesn't give [0 1 2 3 4], but range(5) or range(0,5) does.


def print_board(board_in):
  for row in range(len(board)):
    new_row = " ".join(board[row])
    print new_row


#lets say the person guesses incorrectly and you want to record this, this is how you 
#reference lists in lists:
#it is not board[guess_row, guess_col].
#it is more like index which row, and then within that row, index the column.

board[guess_row][guess_col] = "X"
