#Numpy

'''
A brief tutorial on basic numpy

numpy allows you to work with vectors and matrices a bit more easily
'''

# create a zero vector with length 3

v = np.zeros(3)

# n by m matrix of ones

M = np.ones((3,4))

# array of arrays (a 2x3 array)

A = np.array([[1,2,3],[4,5,6]]) 


#you can also create arrays based on a range (defaultin)

x = np.arange(10) #produces: [0 1 2 3 4 5 6 7 8 9]

#create evenly spaced elements

x = np.linspace(0, 1, num=5) #produces array([ 0.  ,  0.25,  0.5 ,  0.75,  1.  ])

#create arrays in a logspace

x = np.logspace(1,10, num=8)

#random integers

r = np.random.randint(0, 6, size=(4, 3)) #produces 4x3 matrix of values between 0 and 6 (but not including 6)

#crete a matrix of zeros whos dimensions match the input matrix

np.zeros_like(r) #r (from the example above) is 4x3 so this is a zero matrix of 4x3

#generate 4 gaussian random numbrs

np.random.randn(4)   

#set the seed for random number generation

np.random.seed(1)  


#make a vector of the numbrs 0 to 8 and reshape them into a 3x3 matrix

a = np.arange(9).reshape(3,3)


#-------------------------------------------------

#Indexing  (remember python indexing starts from 0!!!)



a[2, 2] # 3rd row, 3rd column
a[1] # 2nd row
a[:, 2] # all rows, 3rd column

a[1:, :2] # from 2nd row to end, and from 1st column up to (but not including the third)

a[0::2,0::2] #this gives the corner elemens

#return the 2nd, 3rd and 5th item in every other row in P, starting with row 0
P = np.random.rand(5, 5)
P[np.repeat((0,2,4),3),np.repeat((1,2,4),3)]

#Generate a 10 x 3 array of random numbers in range [0,1]. For each row, pick the number 
#closest to 0.5
A = np.random.rand(10,3)
c = np.min(np.abs(A-0.5),axis=0)

#Task: You're given two matrices of the same shape. Select values from the first if the 
#values in the second are positive. 
first = np.random.randint(10, size=(10,10))
second = np.random.randn(100).reshape(10,10) - 0.3

inds = second > 0 
first[inds]



#-------------------------------------------------

#Reshaping
z = np.zeros(6)
z.shape # a 1x6 vector

#reshape from a row to a column vector
#note that the transpose operation doesn't seemp to work as you would expect
z.reshape(len(z), 1)

#add an extra dimension to a matrix
z[:, None] #has the same effect as the above operation
z[:, np.newaxis] #another method 

#standard reshaping (dimensions must agree)
z = z.reshape(3, 2)

#reshape, where you know the size of one dimension, but let python figure out
#the size of the other dimension
z = z.reshape(2, -1)

# transpose 
z.T

#unravel a matrix into a 1 dim array
z.ravel() #gives you a view of the unraveld matrix
z.flatten() #gives you a copy of the unraveld matrix









