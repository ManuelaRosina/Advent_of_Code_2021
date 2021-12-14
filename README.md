# Advent_of_Code_2021

This year I'll try to finish the advent of code. Let's see how far I get :)
Here I'll keep trak of my basic idea of my solution.

## Day 1: Sonar Sweep
### Part 1 Problem: 
Given a list of numbers count how often a number is larger than the previous one.

### My solution: 
Loop through the list and compare the two numbers. Increase a counter if the second is larger than the first

### Part 2 Problem:
Now we have to sum all numbers in a window of size 3 and count again how often that sum is larger than the previous one.

### My solution:
I adjusted the loop to stop at the last window (not the last element) and select the numbers from the list inside the window to compute the sum. The rest stays the same.

## Day 2: Dive!
### Part 1 Problem:
Given a list of instructions of the form 'forward/up/down X' where X is a number find the horizontal and depth position after they are executed. 'down' increases depth, 'up' decreased depth, forward increases the horizontal position.

### My solution:
In this case I haven't split the loading of the data and the computation in two parts but do it in one go. For each line in the input I split it on the space. The second part is converted to an int and based on the first part the operation is selected.

### Part 2 Problem:
Now the up and down instructions decrease and increase a value called aim respectively. Forward increases the horizontal value by X and the depth by the current aim multiplied by X.

### My solution:
I used the same code as before but adjusted the computation operations according to the problem description.

## Day 3 Binary Diagnostic:
### Part 1 Problem:
We have a list of binary numbers. We need to find the values called gamma rate and epsilon rate. The bits in the gamma rate are defined as the most common bit over the whole input list at that position. The epsilon rate is the least common bit (the inverse of gamma).

### My solution:
I load the input in a 2D array, which I can then sum over the first axis. This gives us the number of times the 1 bit is used in each position. If this number is larger or equal than half the length of the list the gamma bit is 1 else 0. We can do the same but reverse 1 and 0 for the epsilon value.

### Part 2 Problem:
Now we need to find the values called oxygen generator rating and CO2 scrubber rating. To find those we need to go from the first to the last position and determine the most comman (and least common) bit and keep only the numbers with that bit. Then repeat the process with the resulting sublist and the second bit and so on. We stop when the list contains only one element.

### My solution:
The problem describtion descirbes already part of my solution. I wrote separate functions to compute the most fequent and least fequent bits for a given list. As well as a function that reduces a list and keeps only the numbers that have a given bit value at a given position. I combine those elements in a loop that stops when we only have one element left.

## Day 4: Giant Squid
### Part 1 Problem:
We play bingo. We get a list of drawn numbers and bingo boards (5x5 numbers). We need to determine which bingo board wins first given the list of drawn numbers.

### My solution:
I store the boards in a 3D numpy array. I loop througth the drawn numbers and mark all occurences on the board with -1. Then to check if a board has one I sum over the second and third axis and check if the vector contains the value -5. The index of this value correspons to the index of the winning board.

### Part 2 Problem:
Now we need to determine when the last board wins.

### My solution:
I use the same setup as for the first part but instead of stopping when the first board winns I remove it from the board list until only one is left. When that wins I stop.

## Day 5 Hydrothermal Venture:
### Part 1 Problem:
The input is a list of lines in the form 'x1,y1 -> x2,y2' which are either horizontal, vertical or diagonal. For the first part we only consider horizontal and vertical lines (x1 = x2 or y1 = y2). We need to find the number of points where at least two lines overlap.

### My solution:
I store the input as a 3D array and filter the list for horizontal and vertical lines. Then I create a matrix of size max x and max y value of the input. Then for each line I range over the start and end value and add 1 to the point in the matrix. Finally I rearch for all values larger that 1 and compute the length of the found indices.

### Part 2 Problem:
Now we need to do the same for all lines (not only the horizontal and vertical ones). 

### My solution:
I needed to adapt the loop to distinguish between the three cases to compute a list of x and y ranges that are covered by the line. The ranges are ziped together to change the values in the filed matrix.

## Day 6: Lanternfish

### Part 1 Problem:
We need to model the groth of a lanternfish population. Each fish creates a new fish every 7 days. The new created fish needs 9 days before it can reproduce for the first time. The input is a list of numbers that represent the number of days the fish has left before it reproduces. We need to find the number of fish after 80 days.

### My solution:
I store the input as a numpy array. In a loop (representing each day) I reduce all values by 1 and find the fish that have a value of -1. Those values are set back to 6 and a 8 is appended to the list (representing the new fish). After the loop we determine the length of the list.

### Part 2 Problem:
Now we need to do the same for 256 days.

### My solution:
The solution for the first part is too computationally expensive so I need to find a different approach. Instad of a list I represent the input as a 2D matrix. The first colum is the age of the fish the second is the number of fish with that value.

In each day cycle (loop) I now need to substract 1 of the fist column only. When a row reaches -1 the number of fish are added to the row with age 6. and -1 is changed to 8 (for the new fish).

The advantage to the fist approach is that the matrix has a fixed size all the time and we only have to find one row. In the first part we needed to find a growing number of fish with the same value.

## Day 7: The Treachery of Whales

### Part 1 Problem:
We have to align a number of crab submarines horizontally. We have the horizontal position of each crap. Each step a crab takes costs one fuel. We need to find the cheapest solution.

### My solution:
As the cost of each step is constant the cheapest solution is the median. As this value per definition divides the input values in a lower and upper halve. That way the extrem values will not worsen the overall result.

### Part 2 Problem:
Now the cost of each step becomes changes. Instead, each step costs 1 fuel more than the last.

### My solution:
My intuition is that the optimal value needs to be around the mean value, as it is more optimal to have the crabs further away walk less to the alighnment value. As the mean is not an integer I test the upper and lower bound for the lowest costs.

## Day 8: Seven Segment Search
It get's tricky. This one involved more thinking than programming.

### Part 1 Problem:
The input is a list of letters. Each letter corespons to one part of a seven-segment display.
Each row of the input contains all ten digits in this letter encoding (the wiring), in unknown order, followed by '|' and for more digits (the output). The wiring of each row is different.
The first part of this puzzle is to find the number of occurenc of the digits 1, 4, 7 and 8 in the output.

### My solution:
As those digits have a unique number of segments that is used, we can easily compute the length of each 'digit-word' and count the ones with length 2, 4, 3 and 7.

### Part 2 Problem:
Now we are asked to decode the whole output digits.

### My solution:
To solve this we need to figure out the wiring of each row. I create a matrix which shows for each digit what segments are turned on. The sum on the first axis then give us the length of each digit-word. The sum on the second axis shows us how often each digit is turned on. Three of the segments have a unique count (e, b, f) so these can be easily identified. For the other four two are used in eight digits (c and a) and two are used in seven digits (d and g). 

For the first case we can check which of those segments is used in the digit 1 (which we can identify in the sum over the first axis). Segment c is used in 1 segment a not.
We can do the same to distinguish d and g as d is used in 4 and g not.

## Day 9 Smoke Basin:
### Part 1 Problem:
We have a heatmap of height values between 0 and 9. We need to find all sinks, that are points that have no lower neighbouring points. Diagonal values do not count.

### My solution:
This remembered me of the ant search algorithm. So I started with an implementation of a function that, given a position, returns the positions of the adjecent neighbours that have equal or lower height.

As starting points I choose all maximum values (so all positions of height 9).
One for one I pop one element from the candidate set and test for lower neighbours. If there are any they are appended to the candidate set. If there are none we have found a sink and can append it to the set of sinks.
To avoid loops all visited positions are stored in the visited set and not visited again.

### Part 2 Problem:
We need to find the size of each basin. A basin are all locations that flow down to the sink, including the sink itself but excluding points with height of 9.

### My solution:
We now need to work the other way round. We have a list of the sink positions from the first part. From there we visit each neighbour that is larger and put the positions in a set. We stop when the height at the position is 9. In the end we have a set of all positions that are included in a basin. We can compute the legth to get the size we need.

In the end we have a list of all sizes that we can sort so get the three largest ones.

## Day 10: Syntax Scoring

### Part 1 Problem:
The input consists of lines with multiple open and closing brackets. There are four types of brackets: '()', '[]', '{}' and '<>'. The brackets for chunks where each chunk opend must be closed by the bracket of the same type. However, the chunk does not need to be closed directly but inside a chunck can be multiple chunks as well. The task is to find the lines that contain a chunk closed by the wrong bracket. To determine the solution each type of closing brackets is assigned a score. The solution is the sum of those scores.

### My solution:
line by line I loop through the individual brackets. If it is an open bracket it is appended to a list of open chunks. If its is a closing bracket it is checkt if the last bracket in the list of open chunks is the same type. In case it is the open bracket is removed from the list, as the chunk is closed correctly. If it is not we have found an error and the points are added to the final score, then we can move to the next line.

### Part 2 Problem:
The lines that do not contain errors are incomplete. That means that not all open chunks are closed. we need to determine in which order the chunks need to be closed. Again each bracket type is assigned a score. The score per line is determined by the following steps:

1. start with 0
2. multiply by 5
3. add the score of the bracket
4. repeat 2. and 3. with all brackets

The final score is the median of the list of scores.

### My solution:
To get the incomplete lines I adjusted my solution for part 1 to store the indices of the error lines. I then filter those to be left with the incomplete lines only.
I use the same loop from part 1 and removing the stop when an error is found (there should be none anymore) in the end the open chunks list contains all bakets in the order they need to be closed. So they need to be reversed and the score calculated. I do that in two separate functions. In the end I output the median of all scores.

## Day 11: Dumbo Octopus

### Part 1 Problem:
We get a 10x10 matrix with integer values between 1 and 8 representing the energy level of the dumbo octopus sitting at those positions. If a octopus reaches an energy level greater than 9 it flashes. When a flash happens the neighbouring octopuses energy level is increased by one and the energy of the flashing octopus is back at 0. We have to count the number of flashes after 100 steps.
The description gives the following instructions how to model the behaviour:

You can model the energy levels and flashes of light in steps. During a single step, the following occurs:

- First, the energy level of each octopus increases by 1.
- Then, any octopus with an energy level greater than 9 flashes. This increases the energy level of all adjacent octopuses by 1, including octopuses that are diagonally adjacent. If this causes an octopus to have an energy level greater than 9, it also flashes. This process continues as long as new octopuses keep having their energy level increased beyond 9. (An octopus can only flash at most once per step.)
- Finally, any octopus that flashed during this step has its energy level set to 0, as it used all of its energy to flash.

### My solution:
I made three functions: one for the search of the positions where octupuses have reached an energy level greater than 9 (flash_positions). One for the adjustement of the neighbour energy level (flash) and one to reset the energy level given a list of positions (reset\_ernergy).

In the main loop I add 1 to every element of the matrix and find the positions of flashing octopuses. the length of the position list is added to the number of flashes. The while the list of positions is filled I adjust the energy values accourding to the flashing and search for the next flashing octopuses. All positions of the flashed octopusses are stored to reset the energy to 0 at the end of the while loop.

### Part 2 Problem:
Now we need to find the number of steps it takes until all octopuses flash at the same time.

### My solution:
I just needed to make two adjustements to my code from part one: I switched the for loop to a while loop and use the function numpy.any to test if the matrix contains only zeros. I still need a counter to count how often the loop is executed (number of steps) and return this number instead of the flash number.

## Day 12: Passage Pathing

### Part 1 Problem:
We are given a list of connections. Each row shows the connection between two caves. Together this forms a cave system. caves with lowercase letter names represent small caves and caves with uppercase names are large caves. Large caves can be visited infinite times, small caves only once. We need to find the number of legal path from the start cave to the end cave.

### My solution:
I adjusted a DFS algorithm to append the nodes to the visited set only under conditions. Large caves are never added (so can be visited multiple times) and small caves are only added if it is not the end node. When we reach the end node 1 is returned (as we found a legal path). Otherwise we expand all children and add the returning value. Finally the number of path is returned

### Part 2 Problem:
Now one small cave can be visited twice.

### My solution:
Now small caves are appended to visited if they already appear in the path and the bool twice is False (to prevent multiple small caves). If we are not allowed to visit the small cave because there is already a doubble one we return the number of path.

## Day 13: Transparent Origami

### Part 1 Problem:
Once again we are provided with a list of coordinates, that represent dots on a transparent paper. The input gives also a list of folding instructions. Folding can either be done up or to the left. The number provided together with the folding instruction gives the position where the fold is.
Because the paper is transparent dots are visible through the upper paper.

We are asked to performe the first folding opperation and count the number of visible dots (two overlapping dots are counted as one).

### My solution:
using a numpy array I mark the dot positions with 1. For the folding operation I write one function for the up fold and one for the left fold. The only differnce is the axis where the splitting occurs. I split the paper matrix in two parts using slice notation. One part is fliped along the axis and both parts are added together. Lastly all numbers greater than 1 will be set to 1 again.

### Part 2 Problem:
Now we are asked to performe all operations. If performed correctly an eight letter uppercase code should appear.

### My solution:
I add a function fold that chooses the right fold function based on the instruction (x or y fold). Then I loop over all functions to get the final paper. Because the code was not readable in the numpy matrix with zeros and ones I added a pretty print function to print a string instead.
