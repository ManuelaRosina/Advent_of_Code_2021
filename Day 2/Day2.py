horiz = 0
depth = 0

# parsing input
with open("input_day2.txt") as f:
    for line in f:
        instruction = line.split(' ')
        steps = int(instruction[1])
        
        # dircetly update the variables to avoid second loop
        if instruction[0] == 'forward':
        	horiz += steps
        if instruction[0] == 'up':
        	depth -= steps
        if instruction[0] == 'down':
        	depth += steps
        	
print("horizontal: ", horiz, " depth: ", depth)
print("part 1: ", horiz*depth)


horiz = 0
depth = 0
aim = 0
with open("input_day2.txt") as f:
    for line in f:
        instruction = line.split(' ')
        steps = int(instruction[1])
        if instruction[0] == 'forward':
        	horiz += steps
        	depth += aim*steps
        if instruction[0] == 'up':
        	aim -= steps
        if instruction[0] == 'down':
        	aim += steps
        	
print("horizontal: ", horiz, " depth: ", depth)
print("part 2: ", horiz*depth)

