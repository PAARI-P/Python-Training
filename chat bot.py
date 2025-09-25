dt={1:"good morning bro",
    2:"cr7",
    3:"King kholi"}
print("welcome,how can i help you today?")
while True:
    user=input("you:")
    if user.lower()in ["exit","bye","quit"]:
        print("chatbot:Goodbye!")
        break
    elif user.lower() in ["good morning"]:
        print(dt[1])
    elif user.lower()in ["goat of football"]:
        print(dt[2])
    elif user.lower() in["goat of cricket"]:
        print(dt[3])
    else:
        print("data is not found")
        