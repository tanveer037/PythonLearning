from random import randint


value = randint(1,3)

if value == 1:
    player2_bet = "rock"
elif value == 2:
    player2_bet = "paper"
else: player2_bet = "scissors"

print(player2_bet)


