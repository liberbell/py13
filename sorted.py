pointInGame = [0, -10, 15, -2, 1, 12]
sortedGame = sorted(pointInGame)
print(sortedGame)

children = ["Sue", "Jerry", "Linda"]
print(sorted(children))
print(sorted(["Sue", "jerry", "linda"]))

print(sorted("My favorite friend is Linda".split(), key=str.upper))
print(sorted(pointInGame, reverse=True))

leaderBoard = {211: "CKL", 134: "DIE", 331: "JFK"}
print(sorted(leaderBoard, reverse=True))
print(leaderBoard.get(134))

students = [('alice', 'B', 12), ('eliza', 'A', 16), ('tae', 'c', 15)]
print(sorted(students, key=lambda student:student[0]))
