def isGreater (a,b):
    if(a>b):
        print("First number is greater\n")
    else :
        print("Second number is greater\n")

def IsLesser (a,b):
    pass # It will pass for now without body
j = 9
k = 0

isGreater(k,j)
# default arg
# We can provide a default value while creating a function. 
# This way the function assumes a default value even if a value is not provided in the function call for that argument.

# Example:
def average (a = 9,b = 2): # here a and b is default arg
    print("The average is ",(a+b)/2)

average()    


# Keyword arguments:
# We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. 
# Hence, the the order in which the arguments are passed does not matter.

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Kaushal", lname = "Panchal", fname = "KP")


# Required arguments:
# In case we don’t pass the arguments with a key = value syntax, 
# then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

# name("Peter", "Quill") # we should not do like this 
name( "Kaushal", "Panchal", "KP") # we must do like this this called as required arg


# Variable-length arguments:
# Sometimes we may need to pass more arguments than those defined in the actual function. 
# This can be done using variable-length arguments.


# Arbitrary Arguments:
# While creating a function, pass a * before the parameter name while defining the function. 
# The function accesses the arguments by processing them in the form of tuple.

def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("Kaushal", "Panchal", "KP")
# Keyword Arbitrary Arguments:
# While creating a function, pass a ** before the parameter name while defining the function. 
# The function accesses the arguments by processing them in the form of dictionary.

def name(**name):
    print("Hello",name["fname"],name["mname"],name["lname"])

name (mname = "KP",lname= "Panchal",fname = "kaushal")    

# return Statement
# The return statement is used to return the value of the expression back to the calling function.

def avgReturn (a,b,c):
    return (a+b+c)/3

e = avgReturn(1,2,4)
print(e)
