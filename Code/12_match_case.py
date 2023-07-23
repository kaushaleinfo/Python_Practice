num = int(input("Enter number : "))

match num:
    case 0 :
        print("Number is zero")
    case 4 :
        print("Number is four")
    case _ if (num!=90) :
        print(num,"Is not equal to 90")
    case _ :
        print(num,"Number is not database")                    