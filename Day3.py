import numpy as np

def to_binary(b_number_list):
    number_str = '0b'+ ''.join([str(int) for int in b_number_list])
    number = int(number_str, 2)
    
    return number
    
def most_freq_bit(number_matrix, axis=1):
    gamma = number_matrix.transpose().sum(axis=axis)
    length = number_matrix.transpose().shape[axis]
    gamma = [1 if x >= length/2 else 0 for x in gamma ]
    
    return gamma
    
def least_freq_bit(number_matrix, axis=1):
    gamma = number_matrix.transpose().sum(axis=axis)
    length = number_matrix.transpose().shape[axis]
    gamma = [0 if x >= length/2 else 1 for x in gamma ]
    
    return gamma
    
def reduce_list(number_list, bit, pos):

    return np.array([num for num in number_list if num[pos]==bit])


input_b = []
with open("input_day3.txt") as f:
    for line in f:
    	x = [int(i) for i in line if i != '\n']
    	input_b.append(x)
    
input_b = np.array(input_b)

gamma = most_freq_bit(input_b)
print('gamma: ',gamma) #3259
epsilon = least_freq_bit(input_b)
print('epsilon: ',epsilon)

gamma = to_binary(gamma)
epsilon = to_binary(epsilon)

print('part 1:', gamma*epsilon )

#oxigen #most freq

#co2 #least freq
"""number_list = np.array([[0,0,1,0,0],
[1,1,1,1,0],
[1,0,1,1,0],
[1,0,1,1,1],
[1,0,1,0,1],
[0,1,1,1,1],
[0,0,1,1,1],
[1,1,1,0,0],
[1,0,0,0,0],
[1,1,0,0,1],
[0,0,0,1,0],
[0,1,0,1,0]])"""

pos = 0
number_list = input_b.copy()
while len(number_list) > 1:
    bits = least_freq_bit(number_list, axis=1)
    number_list = reduce_list(number_list, bits[pos], pos)
    pos +=1
    
co2 = number_list[0]

pos = 0
number_list = input_b.copy()
while len(number_list) > 1:
    bits = most_freq_bit(number_list, axis=1)
    number_list = reduce_list(number_list, bits[pos], pos)
    pos +=1
    
oxigen = number_list[0]

print("oxigen: ", oxigen, to_binary(oxigen))
print("CO2: ", co2, to_binary(co2))

print("part 2:", to_binary(oxigen)* to_binary(co2))




