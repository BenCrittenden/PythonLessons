#Lesson4_ConditionalsAndControls.

#The basic boolean operators:

== #is equal to
!= #is not equal to
> #greater than
<= #less than or eaqual to

#True and False are written like that, not all upper or lower

True
False

#not:
TRUE
true 
FALSE 
false 

#and or and not are written as words:

and # &
or # |
not #~ or ! i.e. gives True if answer is False and vice versa

"""
there's an order of operations for boolean operators:

    not is evaluated first;
    and is evaluated next;
    or is evaluated last.

use brackets to be more sure
"""

#if statements have the following form. Note the colon, indent and lack of closing character/end

if 8 < 9:
  print "Eight is less than nine!"

#functions are written using def with if statement inside
#note the use of elif for else if and the colon on each alternative option
#also note the use of return

def using_control_again():
    if (6 < 7):
        return "Success #2"
    elif (6 > 7):
    	return "Failure"
    else:
    	return False

print using_control_once() #not required. would subseqeuntly print the result    

 


