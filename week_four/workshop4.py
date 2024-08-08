


class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password
   
        
#  """ Drive code for task 1 """

# user1 = User("Bob", 1234, "password")
# print(user1.name,user1.pin,user1.password)
    
    def change_name(self, new_name):
        self.name = new_name
    def change_pin(self, new_pin):
        self.pin = new_pin
    def change_password(self, new_password):
        self.password = new_password

#  """ Drive code for task 2 """

# user2 = User("Bob", 1234, "password")
# print(user2.name,user2.pin,user2.password)

# user2.change_name("Bobby")
# user2.change_pin(4321)
# user2.change_password("newpassword")
# print(user2.name,user2.pin,user2.password)


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

#  """ Drive code for task 3 """

# bankuser1 = BankUser("Bob", 1234, "password")
# print(bankuser1.name, bankuser1.pin, bankuser1.password, bankuser1.balance)
    def show_balance(self):
        print(f"{self.name} has an account balance of: {self.balance}")
    def withdraw(self, amount):
        self.balance -= amount
        # self.show_balance()
    def deposit(self, amount):
        self.balance += amount
        # self.show_balance()
        
#  """ Drive code for task 4 """

# bankuser2 = BankUser("Bob", 1234, "password")
# bankuser2.show_balance()
# bankuser2.deposit(1000)
# bankuser2.deposit(850)
# bankuser2.show_balance()
# bankuser2.withdraw(450)
# bankuser2.withdraw(120)
# bankuser2.show_balance()
    def transfer_money(self):
        


        
    
        