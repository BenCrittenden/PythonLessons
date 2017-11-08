#Lesson12_AdvancedTopics1

#Create a dict like this: note the commas.

my_dict = {
  'Name':'Ben',
  'Handicap':18,
  'Home Course':'Oxford'
}

print my_dict.items() #prints all the pairs (as a tuple)
print my_dict.keys() #prints only the keys e.g. name, handicap
print my_dict.values() #prints only the values, e.g. 'Ben', 18, etc

#the order of output is alphabetical order of respective keys, even for the values, which
#don't explicitly show the keys.

#If you want to print the key and it's corresponding value:

for key in my_dict:
  print key, my_dict[key]


#list comprehension. 
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

doubles = [x * 2 for x in range(1, 6)]
print doubles

doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]
print doubles_by_3

#get the numbers between 1 and 15 that are divisible by 3 or 5.
threes_and_fives = [x for x in range(1,16) if x % 3 == 0 or x % 5 == 0]

#list slicing:
l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print l[2:9:2]
#prints: [9, 25, 49, 81]

#let's say that you only want to print the odd numbers in a list. You only need to specify
#the stride (because the default start is 0 and it will default to the end too)

#stride of two, with default start and finish
print l[::2]

#to go backwards do a list with -1 as the stride
backwards = l[::-1]

#defining multiple variables on the same line
str = "ABCDEFGHIJ"
start, end, stride = 1, 6, 2
str[start:end:stride]


#using list slicing to slice up a string
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]
print message #prints the above message backwards and every other charater, which gives: I am a secret message!



#####
"""
Lambda Functions

These are anonymous functions. You basically write a short little function to do
something relatively straight forward, but if you don't use that function over and
over it can save time defining it properly

Examples:
"""
def by_three(x):
  return x % 3 == 0

#can be written as (they do exactly the same thing)
lambda x: x % 3 == 0


#another example in combination with filter
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == 'Python', languages)
#prints ['Python']


#another example: print all the square numbers between 30 and 70 from the range of the
#first 10 square numbers
squares = [x ** 2 for x in range(1,11)]
#note that the following are not acceptable python syntax:
#squares = [range(1,11) ** 2]
#squares = [range(1,11)] ** 2

print filter(lambda x: x >= 30 and x <= 70, squares)


garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

print filter(lambda x: x[::-1] != 'X', garbled)
#prints: I am another garbled message


