# class Player:
#     max_hp = 4000
    
# player1 = Player()
# print(player1.max_hp)
# player2 = Player()
# print(player2.max_hp)

class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.score = 0
        
player1 = Player("Aaron", 1200)
player2 = Player("Irene", 1500)


print("P1:", player1.name, " --HP:", player1.hp, "--SCORE: ", player1.score)
print("P2:", player2.name, " --HP:", player2.hp, "--SCORE: ", player2.score)
player1.hp += 500
player1.score += 25
 
print("P1:", player1.name, " --HP:", player1.hp, "--SCORE: ", player1.score)
print("P2:", player2.name, " --HP:", player2.hp, "--SCORE: ", player2.score)