import itertools

for x in itertools.count(50, 5):
    print(x)
    if x == 10000:
        break
