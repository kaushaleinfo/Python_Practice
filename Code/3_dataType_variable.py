'''
Variable is like a container that holds data.
Very similar to how our containers in kitchen holds sugar, salt etc 
Creating a variable is like creating a placeholder in memory and assigning it some value. 
In Python its as easy as writing:
'''

a = 1
b = 5.5
c = "Harry"
d = True
e = None

print("Data type is ",type(a))
print("Data type is ",type(b))
print("Data type is ",type(c))
print("Data type is ",type(d))
print("Data type is ",type(e))

# By default, python provides the following built-in data types:
# int, float, complex, string, bool, list, tuple, dict
# all data type is object and everything in python is object 

list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)

tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)

dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)
