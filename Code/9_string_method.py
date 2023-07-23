#string is immutable we cannot change directly but we can change by copy string
name = "kausahl"

print(len(name))
print(name.upper())
print(name.lower())

#strip : The strip() method removes any white spaces before and after the string.
str2 = " Silver Spoon "
print(str2.strip())

# rstrip : the rstrip() removes any trailing characters.
strip = "kausahl !!!!"
print(name.rstrip("!"))

# Replace : The replace() method replaces all occurences of a string with another string.

name = "kaushal"
print(name.replace("kaushal", "panchal"))


#split : The split() method splits the given string at the specified instance and returns the separated strings as list items.

name = "kaushal Panchal" 

print(name.split(" "))

# Capitalize :The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. 
# The string has no effect if the first character is already uppercase.

str1 = "hello"
capStr1 = str1.capitalize()
print(capStr1)
str2 = "hello WorlD"
capStr2 = str2.capitalize()
print(capStr2)

# The center() method aligns the string to the center as per the parameters given by the user.

welcome = "Welcome to programming word"
print(welcome.center(50))
print(len(welcome.center(50)))
 
# Count : The count() method returns the number of times the given value has occurred within the given string.
str2 = "Abracadabra"
countStr = str2.count("a")
print(countStr)

# endswith : The endswith() method checks if the string ends with a given value. If yes then return True, else return False.
str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))
# We can even also check for a value in-between the string by providing start and end index positions.
str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

# Find : The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.

str1 = "He's name is Dan. He is an honest man."
print(str1.find("me"))

# Index :The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.

str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("i"))

# isalnum : The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. 
# If any other characters or punctuations are present, then it returns False.

str1 = "WelcomeToTheConsole"
print(str1.isalnum())

# The isalnum() method returns True only if the entire string only consists of A-Z, a-z. 
# If any other characters or punctuations or numbers(0-9) are present, then it returns False.

str1 = "WelcomeToTheConsole1"
print(str1.isalpha())

# islower :  The islower() method returns True if all the characters in the string are lower case, else it returns False.

str1 = "WelcomeToTheConsole"
print(str1.islower())

# Isprintable :  The isprintable() method returns True if all the values within the given string are printable, if not, then return False.

str1 = "WelcomeToTheConsole\r" #\r is not printable char
print(str1.isprintable())

# Isspace : The isspace() method returns True only and only if the string contains white spaces, else returns False.

str1 = " kashal "       #using Spacebar
print(str1.isspace())


# startswith :The startswith() method checks if the string starts with a given value. If yes then return True, else return False.
str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

# swapecase : The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.
str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

