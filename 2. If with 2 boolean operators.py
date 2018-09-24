age=input("What is your age?")
passport=input("Do you have a Dutch passport")
if int(age) > 17 and passport == ("yes") or ("Yes"):
    print("You are allowed to vote")
else:
    print("You are too young to vote")