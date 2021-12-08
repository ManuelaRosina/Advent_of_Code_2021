import numpy as np

with open("input_day7.txt") as f:
    crab = np.array([int(x) for x in f.readline().rstrip().split(',')])
    

print("median: ", np.median(crab))
med = np.full(crab.shape, np.median(crab))
print("fuel cost part 1: ", np.absolute(crab -med).sum())

mean = np.round(crab.mean())
print("mean: ", crab.mean())
#print("fuel cost: ", np.absolute(crab -mean))
#print("fuel cost: ", np.math.factorial(np.absolute(crab -med)))

cost = 0
for i in np.absolute(crab - 490):
	cost += np.array(list(range(1,int(i)+1))).sum()
print("fuel cost part 2: ", cost)

