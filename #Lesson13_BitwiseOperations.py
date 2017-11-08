#Lesson12_BitwiseOperations

"""
each digit in binary can be thought of as a decimal number being on or off:
as you move from left to right, the number that is on or off increases in step of ^2
to get 10, you need 8's bit to be on and 2's bit to be on - no other combination works
thus the binary for 8 is 1010.
For 6 it's 0110 or just 110.
For 34 it would be 32 on, 16 off, 8 off, 4 off, 2 on, 1 off: 100010

8's bit  4's bit  2's bit  1's bit
    1       0       1      0 
    8   +   0    +  2   +  0  = 10 

    0   +   1    +  1   +  0
    0   +   4    +  2   +  0  = 6



It is convention to write binary numbers like this, e.g.: 0b1001, 0b1010, 0b1110

"""

print 0b1,    #1
print 0b10,   #2
print 0b11,   #3
print 0b1 + 0b11  # 1 + 3 = 4
print 0b11 * 0b11 # 3 * 3 = 9


#if you want the binary representation of a decimal number:

print bin(10) #0b1010


#You can use int to print out binary numbers into decimals, the second argument tells int
#what base the number is in

print int("0b11001001",2)


#left and right shifts, effectively shifts the 1s and 0s x places to the right or left
#this creates new numbers and is apparently useful.

shift_right = 0b1100
shift_left = 0b1

shift_right = shift_right >> 2
shift_left = shift_left << 2

print bin(shift_right) #0b11
print bin(shift_left) #0b100

"""
The AND (&) operator looks at each bit (position) if they're both 1, it returns 1. If
either are 0 it returns 0:

     a:   00101010   42
     b:   00001111   15       
===================
 a & b:   00001010   10

0 & 0 = 0
0 & 1 = 0
1 & 0 = 0
1 & 1 = 1
"""

print bin(0b1110 & 0b101) #prints 0b100

"""
The OR (|) operator works in a similar way. If either or both positions are 1, it returns
a 1.

    a:  00101010  42
    b:  00001111  15       
================
a | b:  00101111  47

0 | 0 = 0
0 | 1 = 1 
1 | 0 = 1
1 | 1 = 1

"""

print bin(0b1110 | 0b101) #prints: 0b1111

"""
The XOR (^) only outputs 1 if the bit-wise comparison has one on (1) and one off (1)

    a:  00101010   42
    b:  00001111   15       
================
a ^ b:  00100101   37

0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0
"""

print bin(0b1110 ^ 0b101) #prints 1011

"""
The NOT (~) operator effectively adds 1 and makes the number negative

print ~1    = -2
print ~2    = -3
print ~3    = -4
print ~42   = -43
print ~123  = -124

"""

"""
A bit mask is just a little bit of code that tells you if a specific bit in a 
number was on or off:
"""

num  = 0b1100
mask = 0b0100
desired = num & mask
if desired > 0:
  print "Bit was on"

#They can also be used to turn on a specific bit using |

a = 0b110 
mask = 0b1 
desired =  a | mask # desired = 0b111,

#Similarly, XOR can be used to flip bits

a = 0b11101110
mask = 0b11111111 #flips all bits
print bin(a ^ mask)

#if you want to flip a specific bit, you could use a little function like this
#which utilises the << shift functionality

def flip_bit(number, n):
  mask = (0b1 << n-1)
  result = bin(number ^ mask)
  return result

print flip_bit(0b00001, 3)
