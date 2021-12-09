import numpy as np

def smallest_neigbour(x,y,heatmap):
    low = heatmap[x,y]
    max_x, max_y = heatmap.shape
    lower_points = []
    if x != 0 and heatmap[x-1,y] <= low:
        lower_points.append((x-1,y))
    if x+1 != max_x and heatmap[x+1,y] <= low:
        lower_points.append((x+1,y))
    if y != 0 and heatmap[x,y-1] <= low:
        lower_points.append((x,y-1))
    if y+1 != max_y and heatmap[x,y+1] <= low:
        lower_points.append((x,y+1))
        
    return lower_points
    
def larger_neigbour(x,y,heatmap):
    low = heatmap[x,y]
    max_x, max_y = heatmap.shape
    larger_points = []
    if x != 0 and heatmap[x-1,y] > low:
        if heatmap[x-1,y] != 9:
            larger_points.append((x-1,y))
    if x+1 != max_x and heatmap[x+1,y] > low:
        if heatmap[x+1,y] != 9:
            larger_points.append((x+1,y))
    if y != 0 and heatmap[x,y-1] > low:
        if heatmap[x,y-1] != 9:
            larger_points.append((x,y-1))
    if y+1 != max_y and heatmap[x,y+1] > low:
        if heatmap[x,y+1] != 9:
            larger_points.append((x,y+1))
        
    return larger_points

heatmap = []
with open("input_day9.txt") as f:
    for line in f:
        row = [int(x) for x in line.rstrip()]
        heatmap.append(row)
        
heatmap = np.array(heatmap)    
#print(heatmap)

x_idx,y_idx = np.where(heatmap==heatmap.max())

candidates = set((x,y) for x, y in zip(x_idx,y_idx))
lowest_points = set()
visited = set()

while candidates:
    next_x,next_y = candidates.pop()
    if (next_x,next_y) not in visited:
        smaller = smallest_neigbour(next_x,next_y,heatmap)
        if smaller:
            candidates = set.union(candidates, set(smaller))
        else:
            lowest_points.add((next_x,next_y))
		    
        visited.add((next_x,next_y))

risk_level = 0
for x,y in lowest_points:
    risk_level += heatmap[x,y]+1
print('Part 1: ', risk_level)

sizes = []

for x,y in lowest_points:
    visited = set()
    next_points = set(larger_neigbour(x,y,heatmap))
    sink_size = len(next_points)+1
    while next_points:
        x_next, y_next = next_points.pop()
        visited.add((x_next, y_next))
        next = larger_neigbour(x_next,y_next,heatmap)
        for point in next:
            if point not in visited:
                next_points.add(point)

    sizes.append(len(visited)+1)

print("Part 2: ", np.prod(np.array(sorted(sizes, reverse=True)[:3])))
