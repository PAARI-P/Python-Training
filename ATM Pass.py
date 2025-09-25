correct_password=105114
print("Welcome the ATM!!")
while True:
    password=int(input("Enter the password :"))
    if password==correct_password :
        print("your password is correct,Acess granted")
        break
    else:
        print("Your password is wrong!try again")

