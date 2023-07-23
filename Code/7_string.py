'''
In python, anything that you enclose between single or double quotation marks is considered a string. 
A string is essentially a sequence or array of textual data.
'''

name = "Kaushal"
print("Hello, " + name)

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Looping through the string

for character in a:
    print(character)


# ---  ----    string slicing  --------- ---------- 

string_slicing = "Hello Kaushal"
print(len(string_slicing)) # find lenth of string using len function

print(string_slicing[0:5]) # it will give first 5 character including 0 not 5
print(string_slicing[:5]) # it will give first 5 character
print(string_slicing[2:5]) # it will give 2 index to 5 index character

print(string_slicing[:]) # it will put len of string 
print(string_slicing[:-3]) # python will put automaticlly like this print(string_slicing[0 : len(string - 3])
print(string_slicing[-2:-1]) # python will put automaticlly like this print(string_slicing[len(string -1) : len(string - 3])11 :10

harry = "harry"
print(harry[-4:-2])
# 1:3

