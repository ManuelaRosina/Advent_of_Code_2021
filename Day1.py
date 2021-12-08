
# Read the input: each measurement is on a separate line
measurements = []
with open("input_day1.txt") as f:
    for line in f:
        measurements.append(int(line))

# loop through the list of measurements to count the number of times it is larger than the previous.
i = 0
increase = 0
for m in measurements:
    if m > i:
        increase += 1
        
    i = m
    
print("part 1: ", increase-1) # -1 because the first one has no previous measurement

# adjusted the code for part 2 to sum the elements in the current window first
window_size = 3
x = 0
increase = 0
for i in range(len(measurements) - window_size + 1):
    m = sum(measurements[i: i + window_size])
    if m > x:
        increase += 1
    else:
    x = m
    
print("part 2: ", increase-1)
