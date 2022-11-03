import random
bal = random.randint(100,300)
print("Welcome to Python Bank! Your balance is",bal)
inpt = str("dummy command")
while inpt != "STOP":
    inpt = input(str("What would you like to do? (WITHDRAW, DEPOSIT, STOP) "))
    if inpt == "DEPOSIT":
        dpst = int(input("How much would you like to deposit? "))
        bal = bal+dpst
        print("Your new balance is",bal)
    if inpt == "WITHDRAW":
        wtdr = int(input("How much would you like to withdraw? "))
        bal = bal-wtdr
        print("Your new balance is",bal)
    else:
        "Invalid input. Tip: The commands are case sensitive"
print ("Thank you for using Python Bank!")
