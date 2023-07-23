# List Methods
# list.sort()
# This method sorts the list in ascending order. The original list is updated

colors = ["red","Blue","White","Black"]
print(colors)
colors.sort()
print(colors)

number=[1,2,4,6,22,77,123,677,1232,0]
print(number)
number.sort()
print(number)

# Descending order

number.sort(reverse=True)
print(number)

# reverse()
# This method reverses the order of the list.
colors = ["red","Blue","White","Black"]
print(colors)

#remove index
colors.remove("red")
print(colors)

colors = ["red","Blue","White","Black"]
colors.reverse()
print(colors)

# index()
# This method returns the index of the first occurrence of the list item.

colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.index("green"))

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.index(3))

# count()
# Returns the count of the number of items with the given value.

colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.index("green"))

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.count(1))

# copy()
# Returns copy of the list. 
# This can be done to perform operations on the list without modifying the original list.

colors = ["voilet", "green", "indigo", "blue"]
newlist = colors.copy()
print(colors)
print(newlist)

# append():
# This method appends items to the end of the existing list.

colors = ["voilet", "green", "indigo", "blue"]
colors.append("Appded color")
print(colors)
# insert():
# This method inserts an item at the given index. 
# User has to specify index and the item to be inserted within the insert() method.
name = ["Kaushal","Panchal",2,0,11]

name.insert(2,999)
print(name)

# extend():
# This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.

#add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)

# Concatenating two lists:
# You can simply concatenate two lists to join two lists.

colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)




