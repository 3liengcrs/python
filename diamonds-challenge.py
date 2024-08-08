import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    option = input("Press enter to pick a card, or than Q to quit :")
    
    if option.lower() == "q":
        break
    else :
        card = random.choice(diamonds)
        diamonds.remove(card)
        hand.append(card)
        print("Remainig cards: ",diamonds)
        print("Your hand: ",hand)
        if not diamonds:
            print("There are no more cards to pick.")
             