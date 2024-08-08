def show_homepage():
    dash = "-----------------------------------------"
    print("       === DonateMe Hamepage ===      " )
    print(dash)
    print("| 1. Login      | 2. Register           | ")
    print(dash)
    print("| 3. Donate     | 4. Show Donations     | ")
    print(dash)
    print("|            5. Exit                    | ")
    print(dash)
  
def donate(username):
    total = 0
    donate_amt = float(input("Enter amount to donate: "))
    total += donate_amt
    donate_string = f'{username} donated ${donate_amt}'
    print("Thank you for your donation!")
    return donate_string
  
  
def show_donations(donations):
    print("\n--- All Donations---")
    if not donations:
        print("Currently, there are not donations.")
    else :
        str = "\n".join(donations)
        print(str) 
        