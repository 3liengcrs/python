
def bal(balance):
    print(f"Your balance is: $ {balance}")
    
def deposite(balance):
    amount = int(input("Enter amount to deposit: "))
    return balance + amount
    
def withdraw(balance):
    withdraw_amount = int(input("Enter amount to withdraw: "))
    return balance - withdraw_amount
def logout(name):
    print(f"Goodbye {name}!")