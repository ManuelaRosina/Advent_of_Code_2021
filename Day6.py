import numpy as np

with open("input_day6.txt") as f:
    fish = np.array([int(x) for x in f.readline().rstrip().split(',')])
fish.sort()  
print(fish)  

#print(fish)
#day_vec = np.array([[1]*fish.shape[0],[0]*fish.shape[0]]).transpose()
#print(fish.sum(axis=0))
#print(np.subtract(fish,day_vec))
solution_vecs = []
"""for day in range(34):
    
    fish = fish - 1
    nr_new_fish = len(np.where(fish == -1)[0])
    fish = np.where(fish == -1, 6, fish)
    new_fish = np.array([8]*nr_new_fish)
    if len(new_fish) != 0:
        fish = np.concatenate((fish, new_fish))
    #print("Day: ", day, " nr: ",len(fish))
    unique, counts = np.unique(fish, return_counts=True)
    solution_vecs.append(np.array(list(zip(unique, counts))))

for i, v in enumerate(solution_vecs):
    print('Day: ',i)
    print(v)
    print()"""

unique, counts = np.unique(fish, return_counts=True)
fish = np.array(list(zip(unique, counts)))
fish = np.vstack((fish, [6, 0],[7, 0],[8,0]))
print(fish)

for day in range(256):
    print("Day: ", day)
    day_vec = np.array([[1]*fish.shape[0],[0]*fish.shape[0]]).transpose()
    fish = np.subtract(fish,day_vec)
    nr_new_fish = np.where(fish == -1)[0]
    print(fish)
    if len(nr_new_fish) == 1:
        print("nr new fish: ", fish[nr_new_fish,1][0])
        f = np.argwhere(fish == 6)
        print(f)
        if len(f) >= 1:
            f = 7#f[np.where(f == 0)[0]][0][0]
            print(f)
            fish[f,1] = fish[f,1] + fish[nr_new_fish,1]
            fish = np.vstack((fish,[8, fish[nr_new_fish,1][0]]))
            fish = np.delete(fish, nr_new_fish, 0)
    else:
        fish = np.vstack((fish,[8, 0]))
        #    fish = np.where(fish == -1, 6, fish)
        #    fish = np.vstack((fish,[8, fish[nr_new_fish,1][0]]))
        
        print('new')
        print(fish)
        print()
        if len(fish) > 9:
            break
    #print("Day: ", day, " nr: ",fish.sum(axis=0)[1])
print(fish.sum(axis=0))
    
