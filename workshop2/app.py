from banking_pkg.account import bal , deposite, logout, withdraw
def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    login = print("LOGIN")
    

    name = str(input("Enter name to register: "))
   
    pin = input("Enter PIN : ")
    balance = int(0)
    print(f'{name} has been registered with a starting balance of ${balance}')
    print("") 
    while True:
        print("          === Automated Teller Machine ===          ")
        login = print("LOGIN")
        name_to_validate = input("Enter your name :")
        pin_to_validate = input("Enter your PIN : ")
        if name_to_validate == name and pin_to_validate == pin :
            print("Login successful!")
            break
            print("")
        else :
            print("Invalid credentials!")
            print("")
    while True:
        # atm_menu("Mike")
        print("")
        print("")
        print("          === Automated Teller Machine ===          ")
        print("User: " + name)
        print("------------------------------------------")
        print("| 1.    Balance     | 2.    Deposit      |")
        print("------------------------------------------")
        print("------------------------------------------")
        print("| 3.    Withdraw    | 4.    Logout       |")
        print("------------------------------------------")
        option = input("Choose an option: ")
        if option == "1":
            bal(balance)
        elif option == "2":
            s= int(deposite(balance))
            balance = s
            bal(s)
        elif option == "3":
           w= withdraw(balance)
           balance= w
           bal(w)
        else:
            if option =="4":  
               logout(name)
               break
           
atm_menu("user")