import numpy as np

let_to_num = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7}
num_to_let = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g'}
string_to_num = {'abcefg':0, 'cf':1, 'acdeg':2, 'acdfg':3, 'bcdf':4, 'abdfg':5, 'abdefg':6, 'acf':7, 'abcdefg':8, 'abcdfg':9}

def create_trans_dict(matrix):
    segment_counts = matrix.sum(axis=0)
    number_counts = matrix.sum(axis=1)
    decode_dict = dict()

    seg = np.argwhere(segment_counts == 8).flatten()
    numc = np.argwhere(number_counts == 2).flatten()

    if matrix[numc[0], seg[0]] == 1:
        decode_dict[num_to_let[seg[0]+1]] = 'c'
        decode_dict[num_to_let[seg[1]+1]] = 'a'
    else:
        decode_dict[num_to_let[seg[0]+1]] = 'a'
        decode_dict[num_to_let[seg[1]+1]] = 'c'
        
    seg = np.argwhere(segment_counts == 7).flatten()
    numc = np.argwhere(number_counts == 4).flatten()

    if matrix[numc[0], seg[0]] == 1:
        decode_dict[num_to_let[seg[0]+1]] = 'd'
        decode_dict[num_to_let[seg[1]+1]] = 'g'
    else:
        decode_dict[num_to_let[seg[0]+1]] = 'g'
        decode_dict[num_to_let[seg[1]+1]] = 'd'
        
    decode_dict[num_to_let[np.argwhere(segment_counts == 4).flatten()[0]+1]] = 'e'
    decode_dict[num_to_let[np.argwhere(segment_counts == 6).flatten()[0]+1]] = 'b'
    decode_dict[num_to_let[np.argwhere(segment_counts == 9).flatten()[0]+1]] = 'f'
    
    return decode_dict
    
def translate(num_string, decode_dict):
    trans = ''
    for let in num_string:
        trans += decode_dict[let]
        
    trans = "".join(sorted(trans))
    return string_to_num[trans]
    

def create_matrix(signal_p):
    matrix = np.zeros((10,7))
    for i, sig in enumerate(signal_p):
        for let in sig: 
            matrix[i, let_to_num[let]-1] = 1
            
    return matrix

# parsing
signal_p = []
output = []
with open("input_day8.txt") as f:
    for line in f:
        x, y = line.rstrip().split(' | ')
        signal_p.append(x.split(' '))
        output.append(y.split(' '))

# Part 1:
length = np.array([len(d) for row in output for d in row])      
unique, counts = np.unique(length, return_counts=True)
length = dict(zip(unique, counts))
print("part 1: ", length[2]+length[3]+length[4]+length[7])

# Part 2:

out_sum = 0

for signal, out in zip(signal_p, output):
    matrix = create_matrix(signal)
    decode_dict = create_trans_dict(matrix)
    exp = 1000
    for n in out:
        trans = translate(n, decode_dict)
        out_sum += trans*exp
        exp = exp/10
    
print('part 2:', int(out_sum))
