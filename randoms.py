import random

print(random.random())

decider = random.randrange(2)
print(decider)

if decider == 0:
    print("HEADS")
else:
    print("TAILS")

print(random.random(1, 7))
