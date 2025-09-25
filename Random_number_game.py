import random
a=random.randint(1,10)
attempt=3
while attempt>=1:
    b=int(input("Enter the number :"))
    if(b==a):
        print("You got the Correct answer")
        break
    elif(a>b):
       print("it is low")
    elif(a<b):
        print("it is high")
    else:
        print("invalid number")
        attempt=attempt-1
    if attempt==0:
        print("try again")
    else:
        print("you have",attempt-1,"attempts left")