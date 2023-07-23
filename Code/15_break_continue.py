for i in range(15):
    if(i == 10):
        break
    print("5 X",(i+1), "=", 5*(i+1))
    i+=1;
print("Out of loop\n") # llop ko chood kr nikal jao 

for i in range(15):
    if(i == 10):
        print("Skip this iteration\n")
        continue
    print("5 X",(i+1), "=", 5*(i+1))

# make do while loop
num = 1
while (1):
    print(num)
    num = num + 1
    if(num %100 == 0):
        break    

