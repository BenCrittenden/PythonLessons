#Lesson_7_FunctionsAndLists

#There are several ways to remove items from lists:

n = [1, 3, 5]

n.remove(1)
n.pop(1) #this also returns the item you delete, as well as remove it from n
del(n[1])

print n

#The range function works like this:


range(6) # => [0, 1, 2, 3, 4, 5] #note there's 6 numbers, but not 6 itself because of 0
range(1, 6) # => [1, 2, 3, 4, 5]
range(1, 6, 3) # => [1, 4]


#lists works a bit differently to vectors in matlab.
#here the lists are concatenated, the vectors are NOT added together elementwise

m = [1, 2, 3]
n = [4, 5, 6]

def join_lists(x,y):
  return x + y

print join_lists(m,n) #produces [1, 2, 3, 4, 5, 6] and not [5, 7, 9]




