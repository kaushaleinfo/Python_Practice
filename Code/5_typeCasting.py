a = "1"
# a = 1
b = "2"
# b = 2

print (int(a) + int (b))

# Two Types of Typecasting:
# Explicit Conversion (Explicit type casting in python)
# Implicit Conversion (Implicit type casting in python).

'''
Explicit typecasting:
The conversion of one data type into another data type, done via developer or programmer's manually as per the requirement, 
is known as explicit type conversion.

It can be achieved with the help of Python built-in type conversion functions such as int(), float(), hex(), oct(), str(), etc .
'''

string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)

'''
Implicit type casting:
Data types in Python do not have the same level 
i.e. ordering of data types is not the same in Python. 
Some of the data types have higher-order, and some have lower order. 
While performing any operations on variables with different data types in Python, 
one of the variable's data types will be changed to the higher data type. 
According to the level, one data type is converted into other by the Python interpreter itself (automatically). 
This is called, implicit typecasting in python.

Python converts a smaller data type to a higher data type to prevent data loss.
'''

# Python automatically converts
# a to int
a = 7
print(type(a))
 
# Python automatically converts b to float
b = 3.0
print(type(b))
 
# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))
