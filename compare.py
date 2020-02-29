firstname = "Taylor"
print(len(firstname))

lastname = "Swift"
print(len(lastname))
firstname.__len__()


ages = [0, 11, 22, 45, 87, 4]
print(len(ages))

i = 0
for i in range(0, len(ages)):
    print(ages[i])
