import statistics
import math

agesData = [10, 13, 14, 24, 11, 7, 5, 8, 14]

print(statistics.mean(agesData))
print(statistics.mode(agesData))
print(statistics.median(agesData))

print(sorted(agesData))

print(statistics.variance(agesData))
print(statistics.stdev(agesData))

print(math.sqrt(statistics.variance(agesData)))

print(sorted(agesData, reverse=True))