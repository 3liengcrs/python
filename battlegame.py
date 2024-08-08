### Python week one workshop assignment ###

#TASK 1: SET UP THE GAME

# 1- Declare three variable with the following names

wizard = "Wizard"
elf = "Elf"
human = "Human"

# 2- Declare three variable, set to integer values that indicate the HP

wizard_hp = 70
elf_hp = 100
human_hp = 150

# 3-Declare three more variable having integer values that indicate the damage of each character

wizard_damage = 150
elf_damage = 100
human_damage = 20

# 4-Variables for Dragon
 
dragon_hp = 300
dragon_damage = 50

# TASK 2

while True:
    # Displaying options for the player to choose from
    print("Options:")
    print("1) Wizard")
    print("2) Elf")
    print("3) Human")
    
# TASK 3
    choice = input("Choose your character: ")
    
    # Handling the player's choice
    if choice == '1':
        character = "Wizard"
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif choice == '2':
        character = "Elf"
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif choice == '3':
        character = "Human"
        my_hp = human_hp
        my_damage = human_damage
        break
    else:
        print("Unknown character")

#TASK 4


while True:
    # Reducing dragon's hit points by the value of my_damage
    dragon_hp -= my_damage
    
    # Printing battle progress
    print(f"{character} attacks the Dragon!")
    print(f"The Dragon's hit points: {dragon_hp}")
    
    # Checking if the Dragon has lost the battle
    if dragon_hp <= 0:
        print("The Dragon has lost the battle")
        break

# The battle has concluded

 