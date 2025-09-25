name=input("Name of student=")
age=int(input("Age of student="))
Tamil=int(input("enter the mark of Tamil="))
English=int(input("enter the mark of English="))
Maths=int(input("enter the mark of Maths="))
Total =Tamil+English+Maths
print("Total",Total)
average = Total//3
print("average",average)
if average>=85:
    print("first class")
elif average>=65:
    print("second class")
elif average>=64:
    print("third class")
elif average<50:
    print("fail")
else:
    print("enter the valid mark")
              
              