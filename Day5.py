import numpy as np

def filter_lines(lines):
    return np.array([elem for elem in lines if elem[0][1] == elem[1][1] or elem[1][0] == elem[0][0]])
    
def horiz_vert(lines):
    horizontal = []
    vertical = []
    for elem in lines:
        if elem[1][0] == elem[0][0]:
            vertical.append(elem)
        if elem[0][1] == elem[1][1]:
            horizontal.append(elem)
    return np.array(horizontal), np.array(vertical)
    
def adap_range(start, stop):
    if start == stop:
        return None
    if start < stop:
        return range(start,stop+1)
    else:
        return range(start,stop-1,-1)

lines = []
with open("input_day5.txt") as f:
    for line in f:
        lines.append([[int(n) for n in x.split(',')] for x in line.rstrip().split(' -> ')])
        
print(np.array(lines).max(axis=(0,1)))

fiels_shape = np.array(lines).max(axis=(0,1))
field = np.zeros([fiels_shape[0]+1,fiels_shape[1]+1])
#print(field)

"""horiz, vert = horiz_vert(filter_lines(lines))

for line in horiz:
    y = line[1][1]
    x_range = [line[1][0], line[0][0]]
    x_range.sort()
    for x in range(x_range[0], x_range[1]+1):
        field[y][x] += 1
        
for line in vert:
    x = line[0][0]
    y_range = [line[0][1], line[1][1]]
    y_range.sort()
    for y in range(y_range[0], y_range[1]+1):
        field[y][x] += 1
#print(field)

print("part 1: ", len(np.where(field > 1)[0]))"""

for line in lines:
    x_range = adap_range(line[0][0], line[1][0])
    y_range = adap_range(line[0][1], line[1][1])
    if not x_range:
        x_range = [line[0][0]]*len(y_range)
    if not y_range:
        y_range = [line[1][1]]*len(x_range)
    for x,y in zip(x_range, y_range):
        field[y][x] += 1
            
print("part 2: ", len(np.where(field > 1)[0]))
