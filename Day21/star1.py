class Dice:

    def __init__(self):
        self.value = 0
        self.rolled = 0

    def roll(self):
        self.rolled += 1
        self.value = self.value % 100 + 1
        return self.value    

players = [[7, 0], [8,0]] # [player1[position, score], player2(pos, score)]

dice = Dice()
i = 0
while True:
    players[i][0] = (players[i][0] + dice.roll() + dice.roll() + dice.roll() -1) % 10 +1 
    players[i][1] += players[i][0]
    if players[i][1] >= 1000:
        print(players[(i+1)%2][1] * dice.rolled)
        break
    i = (i+1) %2 