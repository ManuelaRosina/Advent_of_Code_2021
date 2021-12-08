import numpy as np

def remove_board(board_list, pos):
    return np.array([board for i, board in enumerate(board_list) if i not in pos])

def parse_input():
    with open("input_day4.txt") as f:
        numbers = [int(i) for i in f.readline().rstrip().split(',')]
        
        boards_matrix = []
        for line in f:
            board = []
            for i in range(5):
                row = [int(i) for i in f.readline().rstrip().split(' ') if i != '']
                board.append(row)
            boards_matrix.append(board)
            
    boards_matrix = np.array(boards_matrix)        
    return boards_matrix, numbers
    
#Part 1:
boards_matrix, numbers = parse_input()
for i in numbers:
    boards_matrix = np.where(boards_matrix == i, -1, boards_matrix)
    columns = boards_matrix.sum(axis=1)
    rows = boards_matrix.sum(axis=2)
    
    if -5 in columns:
        winning_b = np.where(columns == -5)[0][0]
        last_nr = i
        break
    if -5 in rows:
        winning_b = np.where(rows == -5)[0][0]
        last_nr = i
        break

winning_b = boards_matrix[winning_b]
winning_b = np.where(winning_b == -1, 0, winning_b)
print("part 1: ", winning_b.sum()*last_nr)

#Part 2:
boards_matrix, numbers = parse_input()
final_b = False

for i in numbers:
    remove_b = False
    boards_matrix = np.where(boards_matrix == i, -1, boards_matrix)
    columns = boards_matrix.sum(axis=1)
    rows = boards_matrix.sum(axis=2)
    if -5 in columns:
        winning_b = np.where(columns == -5)[0]
        if not final_b:
            remove_b = True
        else:
            last_nr = i
            break

    if -5 in rows:
        winning_b = np.where(rows == -5)[0]
        if not final_b:
            remove_b = True
        else:
            last_nr = i
            break

    if remove_b:
        boards_matrix = remove_board(boards_matrix, winning_b)     
    if boards_matrix.shape[0] == 1:
        final_b = True
      
boards_matrix = np.where(boards_matrix == -1, 0, boards_matrix)   
print("part 2: ", boards_matrix.sum()*last_nr)        
