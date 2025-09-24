a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
operation=input("add,sub,mul,div:")
def calculator(a,b):
  if(operation=="add"):
    print(a+b)
  elif(operation=="sub"):
    print(a-b)
  elif(operation=="mul"):
    print(a*b)
  elif(operation=="div"):
      if(b==0):
          print("invalid")
      else:
          print(a/b)
  else:
     print("the number is invalid")
calculator(a,b)
      
