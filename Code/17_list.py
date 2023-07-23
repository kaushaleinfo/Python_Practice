# Lists are ordered collection of data items.
# They store multiple items in a single variable.
# List items are separated by commas and enclosed within square brackets [].
# Lists are changeable meaning we can alter them after creation.


lst = [1,2,4,5,6,"kaushal"]
print(lst)

lst2 = ["Red", "Green", "Blue"]
print(lst2[2])

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]

# Check whether an item in present in the list?
# We can check if a given item is present in the list. This is done using the in keyword.

if "Red" in colors:
    print("Yes Red is in our database\n")
else:
    print("Red is not database\n")

# Range of Index:
# You can print a range of list items by specifying where you want to start, 
# where do you want to end and if you want to skip elements in between the range.

# listName[start : end : jumpIndex]

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[::2]) # print alternative 

print(animals[0:7])	#using positive indexes
print(animals[-7:-2])	#using negative indexes'

# List Comprehension
# List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.

# List = [Expression(item) for item in iterable if Condition]

# Expression: It is the item which is being iterated.

# Iterable: It can be list, tuples, dictionaries, sets, and even in arrays and strings.

# Condition: Condition checks if the item should be added to the new list or not.

# Example 1: Accepts items with the small letter “o” in the new list
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa","Kaushal"]
namesWith_O = [item for item in names if "o" in item]  # if list contains the specefic data in list then it will be added 
namesWith_O = [item for item in names]
print(namesWith_O)

# Example 2: Accepts items which have more than 4 letters
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if(len(item))>4]
print(namesWith_O)

