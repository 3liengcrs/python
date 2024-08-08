from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register


database = {"admin" : "password123"} 
donations = []
autorized_user = ""
while True:
        print("")
        show_homepage()
        if autorized_user == "":
            print("You must be logged in to donate.")
        else :
            print("Logged in as:", autorized_user)

        option = int(input("Choose in option : "))
        if option == 1 :
                username = input("Enter username: ")
                password = input("Enter password: ")
                print("\n")
                autorized_user = login(database, username, password)
        elif option == 2:
                username = input("Enter username: ")
                password = input("Enter password: ")
                print("\n")
                autorized_user = register(database,username)
                if autorized_user !="":
                    database[username]=password
                    
                    
        elif option == 3:
                if autorized_user == '':
                    print("You are not logged in")
                else :
                    donation_string = donate(autorized_user)
                    donations.append(donation_string)
        elif option == 4:
                print(show_donations(donations))
        elif option == 5:
                print("Leaving DonateMe...")
                print('')
                break
        else :
                print("Invalid option. Please choose a number between 1 and 5.")

