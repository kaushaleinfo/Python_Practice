import time

timeStamp = int(time.strftime('%H'))
print(timeStamp)

if (timeStamp >=0 and timeStamp <=12 ):
    print("Good Morining Sir")
elif (timeStamp >=12 and timeStamp <= 20):
    print("Good Eveining Sir\n")
elif (timeStamp >=21 and timeStamp <= 24):       
    print("Good Night Sir\n")
else:
    print("Time is not supported\n")    

