import numpy as np

def flash_positions(energy):
	x_idx,y_idx = np.where(energy > 9)
	positions = [(x,y) for x,y in zip(x_idx,y_idx)]
	return positions
	
	
def flash(energy, positions, flashed):
	for x,y in positions:
		if (x,y) not in flashed:
			if x != 9:
				energy[x+1,y] += 1
			if x != 0:
				energy[x-1,y] += 1
			if y != 9:
				energy[x,y+1] += 1
			if y != 0:
				energy[x,y-1] += 1
			if x != 9 and y != 9:
				energy[x+1,y+1] += 1
			if x != 9 and y != 0:
				energy[x+1,y-1] += 1
			if x != 0 and y != 0:
				energy[x-1,y-1] += 1
			if x != 0 and y != 9:
				energy[x-1,y+1] += 1
			
	energy = reset_ernergy(energy, positions)
	return energy
	
def reset_ernergy(energy, positions):		
	for x,y in positions:
		energy[x,y] = 0	
	return energy
	
def part_1(energy):
	nr_of_flashes = 0
	for i in range(100):
		energy += 1
		positions = flash_positions(energy)
		flashed = []
		nr_of_flashes += len(positions)
		while positions:
			energy = flash(energy, positions, flashed)
			flashed.extend(positions)
			positions = flash_positions(energy)
			nr_of_flashes += len(positions)
		energy = reset_ernergy(energy, flashed)

	return nr_of_flashes
	
def part_2(energy):
	nr_of_flashes = 0
	i = 0
	while energy.any():
		energy += 1
		positions = flash_positions(energy)
		flashed = []
		nr_of_flashes += len(positions)
		while positions:
			energy = flash(energy, positions, flashed)
			flashed.extend(positions)
			positions = flash_positions(energy)
			nr_of_flashes += len(positions)
		energy = reset_ernergy(energy, flashed)
		i += 1
		
	return i


energy = []
with open("input_day11.txt") as f:
    for line in f:
        row = [int(x) for x in line.rstrip()]
        energy.append(row)
        
energy = np.array(energy)    

nr_of_flashes = 0
print('before any steps: ')
print(energy)
print()
print('part 1:', part_1(energy.copy()))
print('part 2:', part_2(energy))
