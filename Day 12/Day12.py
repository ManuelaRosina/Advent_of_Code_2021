def is_big(self):
    return self.name.isupper()

def flatten(t):
    return [item for sublist in t for item in sublist]
    
def get_cave_dict(connections):
    cave_names = set(flatten(connections))  

    cave_dict = dict()
    for name in cave_names:
        cave_dict[name] = []

    for a,b in connections:
        if b != 'start':
            cave_dict[a].append(b)
        if a != 'start':
            cave_dict[b].append(a)
    
    cave_dict['end'] = []   
    return cave_dict

# Part 1    
def dfs(visited, graph, node, path='', nr_path=0):
    if node not in visited:
        if not node.isupper() and node != 'end':
            visited.add(node)
        if not graph[node]:
            return 1
            
        for neighbour in graph[node]:
            nr_path += dfs(visited.copy(), graph, neighbour, path+' '+node)
            
    return nr_path


def is_small_cave(node):
    return not node.isupper() and node not in ['start', 'end']
    
# Part 2    
def dfs_2(visited, graph, node, paths, path='', nr_path=0, twice=False):
    if node not in visited:
        if is_small_cave(node) and node in path.split(' '):
            if not twice:
                twice = True
            else:
                return nr_path
            
        if twice and is_small_cave(node):
            visited.add(node)
            
        if not graph[node]:
            paths.add(path+' '+node)
            return 1
            
        for neighbour in graph[node]:
            nr_path += dfs_2(visited.copy(), graph, neighbour, paths, path+' '+node, twice= twice)
       
    return nr_path
    
with open('input_day12.txt') as f:
    connections = [x.rstrip().split('-') for x in f.readlines()]

cave_dict = get_cave_dict(connections)       

visited = set() # Set to keep track of visited nodes.

# Part 1
nr_path = dfs(visited.copy(), cave_dict, 'start')
print('part 1: ', nr_path)

paths = set()
nr_path = dfs_2(visited.copy(), cave_dict, 'start', paths)
print()

print('part 2: ', nr_path)
