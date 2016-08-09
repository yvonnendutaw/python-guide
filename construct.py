#!/usr/bin/env python2

#asking the userfor input and storing it in a collection
#used for thesys.exit function
import sys

#varible contains a string whichwill need to be converted
target_int = raw_input("how many integers?")

try:
    target_int=int(target_int)
except:
    sys.exit("you must enter an interger")

ints=list()

count=0

#keeps asking for an integer until the w acquire the target
while count < target_int:
    new_int=raw_input('please enter integer{0}:'.format(count+1))
    isint=False
    try:
        new_int=int(new_int)
    except:
        print("you must enter an integer")

    if isint==True:
        #adds the integer to the collection
	ints.append(new_int)
        #increment count by 1        
	count+=1

print ("using a for loop")
for value in ints:
   print (str(value))
