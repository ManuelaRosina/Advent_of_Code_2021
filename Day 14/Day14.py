from collections import Counter, defaultdict
import numpy as np
from numpy.linalg import matrix_power
import time


def poly_to_chunk(polystring):
    chunks = []
    for i in range(len(polystring) - 1):
        chunks.append(polystring[i: i + 2])
        
    return chunks
    
def create_matrix(chunks):
    poly_matrix = np.zeros((len(chunks), len(chunks)))
    chunk_list = list(chunks.keys())
    index_map = dict()
    for i,c in enumerate(chunk_list):
        index_map[c] = i
    #print(index_map)
    
    for i,c in enumerate(chunk_list):
        #print(c, ': ')
        for p in chunks[c]:
            #print(p, ': ', i, index_map[p])
            poly_matrix[i, index_map[p]] = 1
            
    return poly_matrix, index_map
    
def create_vector(poly_pieces, index_map):
    poly_vec = np.zeros((1,len(index_map)))
    for p in poly_pieces:
        poly_vec[0,index_map[p]] += 1
        
    return poly_vec

def create_letter_idx_map(index_map):
    letter_idx_map = defaultdict(list)
    for chunk in index_map.keys():
        letter_idx_map[chunk[0]].append(index_map[chunk])
        
    return letter_idx_map

def insertion(chunk, iteration, max_it, polystring):
    if iteration == max_it:
        return chunk
    else:
        expanded = chunks[chunk]
        left = insertion(expanded[0], iteration+1, max_it, polystring)
        right = insertion(expanded[1], iteration+1, max_it, polystring)
        return left + right[1:]
        

insertions = dict()
with open('input_day14.txt') as f:
    polymer = f.readline().rstrip()
    f.readline()
    for line in f:
        pair = line.rstrip().split(' -> ')
        insertions[pair[0]] = pair[1]
        
#print(polymer)
#print(insertions)

chunks = dict()

# instead of the inserted letter get a list of the two new pairs
for key, value in insertions.items():
    pieces = [key[0]+value, value+key[1]]
    chunks[key] = pieces

# split the input poly in all possible pairs    
pieces = poly_to_chunk(polymer) 

# the first letter does not change
expanded_poly = pieces[0][0]
max_iter = 10
for p in pieces:
    expanded_poly += insertion(p, 0, max_iter, '')[1:]
sorted_scores = sorted(list(Counter(expanded_poly).values()))
print('part 1: ', sorted_scores[-1]- sorted_scores[0])

start = time.time()
poly_matrix, index_map = create_matrix(chunks)
letter_idx_map = create_letter_idx_map(index_map)
poly_vector = create_vector(pieces, index_map)

iterations = 40
chunk_vec = poly_vector.dot(matrix_power(poly_matrix,iterations))

scores = dict()
for letter in letter_idx_map.keys():
    score = 0
    for idx in letter_idx_map[letter]:
        score += chunk_vec[0, idx]
    scores[letter] = int(score)

scores[polymer[-1]] += 1    
sorted_scores = sorted(list(scores.values()))
stop = time.time()
print('part 2: ', sorted_scores[-1]- sorted_scores[0])
print(f'Part 2 Time: {stop - start}')
