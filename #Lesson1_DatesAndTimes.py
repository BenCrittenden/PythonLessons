#Dates and times

#to add the datetime library:

from datetime import datetime


#to get the current date and time
now = datetime.now()

#the date given looks something like:  2013-11-25 23:45:14.317454
#if we just want the day, month or year we do

day = now.day
month  = now.month
year = now.year

#say you want to convert the date to mm/dd/yyyy and print it

print '%s/%s/%s' % (now.month, now.day, now.year)

#and the same for hours, minutes and seconds:

print '%s:%s:%s' % (now.hour, now.minute, now.second)