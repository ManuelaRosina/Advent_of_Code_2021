import numpy as np

def create_dots(positions):
    paper = np.zeros(positions.max(axis=0)+1).transpose()
    for x,y in positions:
        paper[y,x] = 1
        
    return paper

def fold_up(paper, y):
    part_1 = np.flip(paper[:y, :], axis= 0)
    part_2 = paper[y+1:, :]
    new_paper = part_1 + part_2
    new_paper = np.where(new_paper > 1, 1, new_paper)
    return np.flip(new_paper, axis= 0)

def fold_left(paper, x):
    part_1 = paper[:, :x]
    part_2 = np.flip(paper[:, x+1:], axis=1)

    new_paper = part_1 + part_2
    new_paper = np.where(new_paper > 1, 1, new_paper)
    
    return new_paper

def fold(paper, instr, val):
    if instr == 'x':
        return fold_left(paper, val)
    if instr == 'y':
        return fold_up(paper, val)

def pretty_print(paper):
    str_paper = []
    for row in paper:
        row_string = []
        for number in row:
            if number == 1:
                row_string.append('#')
            else:
                row_string.append('.')
                
        str_paper.append(row_string)
        
    return str_paper
    
positions = []
instructions = []
with open('input_day13.txt') as f:
    for line in f:
        if line.startswith('fold'):
            i = line.rstrip().split('=')
            instructions.append((i[0][-1], i[1]))
        elif line != '\n':
        
            positions.append([int(x) for x in line.rstrip().split(',')])

positions = np.array(positions)
paper = create_dots(positions)
new_paper = fold(paper, instructions[0][0], int(instructions[0][1]))
    
print('Part 1: ', int(new_paper.sum()))

for inst, v in instructions:
    paper = fold(paper, inst, int(v))
    
str_paper = pretty_print(paper)

print('Part 2:')
for row in str_paper:
    print(''.join(row))
