#Lesson15_fileIO

#A bsic script demonstating how to write information to a file

my_list = [i ** 2 for i in range(1, 11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")

for item in my_list:
  f.write(str(item) + "\n")

f.close()


#To read and write to a file use the argument r+ in the open function

my_file = open('output.txt','r+')

#to write to a file, you must pass the .write method a string

my_file.write('text to write here')

#once done with the file, you must also close it using the .close method

my_file.close()


#heres a little code that writes some text from a list, one line at a time
#and then closes the file.

my_list = [i ** 2 for i in range(1, 11)]

my_file = open("output.txt", "w")

for i in my_list:
  my_file.write(str(i) + '\n')
  
my_file.close()


#to read in data, you use the .read() method. This reads in the whole file at once

my_file = open('output.txt','r')

print my_file.read()

my_file.close()

#to only read in one line at a time use .readline() method
#it automatically moves to the next line

my_file = open('text.txt','r')

print my_file.readline()
print my_file.readline()
print my_file.readline()

my_file.close()


#It's very important to close files otherwise the information is stored in a buffer
#and if writing, doesn't actually get written to the file

#there is another way of opening and writing files, that doesn't require you to
#explicitly close a file. This alternative makes use of with and as like so:

with open("text.txt", "w") as textfile:
  textfile.write("Success!")


#to check if a file has been closed you use .closed:

with open("text.txt", "w") as my_file:
  my_file.write("Does this work?")
  
closed = my_file.closed

if closed == False:
  my_file.close()
  
print my_file.closed


