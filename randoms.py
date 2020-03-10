import random

print(random.random())

decider = random.randrange(2)
print(decider)

if decider == 0:
    print("HEADS")
else:
    print("TAILS")

print(random.randrange(1, 7))
print("You rolled a " + str(random.randrange(1, 7)))

lotteryWinner = random.sample(range(100), 5)
print("Lottery Winner is " + str(lotteryWinner))

possiblePets = ["cat", "dog", "fish"]
print(random.choice(possiblePets))

cards = ["Jack", "Queen", "King", "Ace", "Joker"]
random.shuffle(cards)
print(cards)

rannum = random.randrange(1, 100)
print(rannum)