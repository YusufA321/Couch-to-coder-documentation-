pin = 4356
balance = 21000
input_pin = input("Enter PIN ")

if(pin == int(input_pin)):
    user_choice = input("Would you like to Deposit or Withdraw?")
    if(user_choice == "withdraw"):
        amount = input("How much would you like to Withdraw?")
        balance -= int(amount)
        print("Your new Balance is " + str(balance))

    if(user_choice == "deposit"):
        amount = input("How much would you like to Deposit?")
        balance += int(amount)
        print("Your new Balance is " + str(balance))

else:
    print("Acess denied. Incorrct PIN")


#Conditional flows with a bank ATM system.
#Worked on an assignment where we understood bank ATMs using python and I got to build one myself.
#The task was to make a pin number at a bank ATM where I used control flows for example: if the pin number is correct access to money.
#If not, cannot access money.
#I eventually improved it by implementing a complete withdraw and deposit system with money which has a bank balance.
