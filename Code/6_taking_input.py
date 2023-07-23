'''
In python, we can take user input directly by using input() function.
This input function gives a return value as string/character 
hence we have to pass that into a variable
'''

a = input("Enter your name : ")
print("Your Entered name : ",a)

b = input ("Enter first number : ") 
c = input ("Enter Second number : ")

d = b + c

print("Output is ",d)

e = int(input("Enter your number "))
f = int(input("Enter your number "))
print("After typecasting into int ",e + f)
