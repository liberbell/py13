pointInGame = [0, -10, 15, -2, 1, 12]
sortedGame = sorted(pointInGame)
print(sortedGame)

children = ["Sue", "Jerry", "Linda"]
print(sorted(children))
print(sorted(["Sue", "jerry", "linda"]))

print(sorted("My favorite friend is Linda".split(), key=str.upper))
