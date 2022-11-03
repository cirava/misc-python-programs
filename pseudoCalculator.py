#This is really over-engineered and would have been easier with a while loop, but this was made before I learned while
#loops in my class, so here is something that could probably be under 30 lines long that is 50 lines long. Oh well.
print("Welcome to the Python Pseudo Calculator™!")
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
oprtr = str(input("What would you like to do to these numbers? "))
if oprtr == "Add" or oprtr == "add" or oprtr == "Addition" or oprtr == "addition":
    ans1 = (num1+num2)
    print("The sum is:",ans1)
elif oprtr == "Subtract" or oprtr == "subtract" or oprtr == "Subtraction" or oprtr == "subtraction":
    ans1 = (num1-num2)
    print("The difference is:",ans1)
elif oprtr == "Multiply" or oprtr == "multiply" or oprtr == "Multiplication" or oprtr == "multiplication":
    ans1 = (num1*num2)
    print("The product is:",ans1)
elif oprtr == "Divide" or oprtr == "divide" or oprtr == "Division" or oprtr == "division":
    ans1 = (num1/num2)
    print("The product is:",ans1)
else:
    print("Invalid input. The \"original number\" has been set to 1 since you\ncan't type in an operater right")
    ans1 = 1
ext1 = str(input("Would you like to enter another number? (Y/N) "))
if ext1 == "Y" or ext1 == "y":
    num3 = int(input("Enter another number: "))
    oprtr2 = str(input("What would you like to do your original number? "))
    if oprtr2 == "Add" or oprtr2 == "add" or oprtr2 == "Addition" or oprtr2 == "addition":
        ans2 = (ans1+num3)
        print("The sum is:",ans1+num3)
    elif oprtr2 == "Subtract" or oprtr2 == "subtract" or oprtr2 == "Subtraction" or oprtr2 == "subtraction":
        ans2 = (ans1-num3)
        print("The difference is:",ans1-num3)
    elif oprtr2 == "Multiply" or oprtr2 == "multiply" or oprtr2 == "Multiplication" or oprtr2 == "multiplication":
        ans2 = (ans1*num3)
        print("The product is:",(ans1*num3))
    elif oprtr2 == "Divide" or oprtr2 == "divide" or oprtr2 == "Division" or oprtr2 == "division":
        ans2 = (ans1/num3)
        print("The product is:",ans1/num3)
    else:
        print("Invalid input. No point in worrying about the value this time\nsince the next input is played as a phony.")
    ext2 = str(input("Would you like to enter another number? (Y/N) "))
    if ext2 == "Y" or ext2 == "y":
        print("Too bad! I'm done now.")
    elif ext2 == "N" or ext2 == "n":
        print("Good! I was done anyways.")
    else:
        print("Your invalid input dissappointed me so much that I decided to stop the program just because of you.")
elif ext1 =="N" or ext1 == "n":
    print("Thank you for using my calculator!")
else:
    print("Invalid input, restart I guess.")
