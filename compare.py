firstname = "Taylor"
print(len(firstname))

lastname = "Swift"
print(len(lastname))
firstname.__len__()


ages = [0, 11, 22, 45, 87, 4]
print(len(ages))
print(sorted(ages))

i = 0
for i in range(0, len(ages)):
    print(ages[i])

print(len(["bob", "mary", "sam"]))

candycollection = {"bob": 10, "mary": 7, "sam": 18}
print(len(candycollection))
