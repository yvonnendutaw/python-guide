#!/usr/bin/env python2
#this function accepts a variable that will be called original in the scope

def modify_string(original):
    original += "that has been modified"
#here only the local copy has been modified


def modify_string_return(original):
    original += "that has been modified"
    return original
#returns th local copy to the caller
#function ends as soon as return statement is called.

test_string = "this is a test string"

#calling the modify_string function
modify_string(test_string)
print(test_string)


#calling the modify_string_return function
test_string = modify_string_return(test_string)
print test_string
