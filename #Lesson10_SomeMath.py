#Lesson9_SomeMath

#This uses the numpy library, which needs to be imported in order to be able
#to add a single number to every element in a list. This doesn't work with normal
#lists

from numpy import array

def factorial(x):
  nums = array(range(x)) + 1
  total = 1
  print nums
  for i in nums:
    total = total * i
    
  return total

print factorial(4)




"""
add every digit within a number. First need to convert the number to a string so that
I can access the individual numbers. Then I can do the addition.
"""

def digit_sum(n):
  num_str = str(n)
  total = 0
  for i in num_str:
    total = total + int(i)
  
  return total

print digit_sum(1234) 



#A code to calculate primes (-neg numbers are not prime, neither are 0 or 1, by definition)

def is_prime(x):
  if x < 2:
    return False
  else:
    for n in range(2,x-1):
      if x % n == 0:
        print 'Factor', n
        return False
    else:
      return True
    
print is_prime(127)



#A scrabble score calculator utilising a dictionary

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
  word = word.lower()
  total_score = 0
  for letter in word:
    total_score += score[letter]
    
  return total_score

print scrabble_score('quizzical')


#a script that splits strings up and also uses enumerate in a for loop
#
def censor(text,word):
  sentence_list = text.split()

  new_sentence = ''
  for idx, w in enumerate(sentence_list):
    if w == word:
      word_len = len(w)
      new_sentence += '*' * word_len
    else:
      new_sentence += w
    
    print idx 
    print (len(sentence_list))
    if idx < len(sentence_list) - 1:
      new_sentence += ' '
    
  return new_sentence

print censor('go fuck yourself','fuck')


#take a list and only return the even numbers. uses append

def purify(all):
  evens = []
  for i in all:
    if i % 2 == 0:
      evens.append(i)
      
  return evens
  
  
print purify([1,2,3,4,5]) 

#mulitply all of the elements in a list. uses *=

def product(input):
  running_total = 1
  for i in input:
    running_total *= i
  
  return running_total

  