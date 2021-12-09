# Advent_of_Code_2021

This year I'll try to finish the advent of code. Let's see how far I get :)
Here I'll keep trak of my basic idea of my solution.

## Day 1: Sonar Sweep
### Part 1 Problem: 
Given a list of numbers count how often a number is larger than the previous one.

### My solution: 
loop through the list and compare the two numbers. Increase a counter if the second is larger than the first

### Part 2 Problem:

### My solution:  

## Day 2: Dive!
### Part 1 Problem:
Given a list of instructions of the form 'forward/up/down X' where X is a number find the horizontal and depth position after they are executed. 'down' increases depth, 'up' decreased depth, forward increases the horizontal position.

### My solution:

### Part 2 Problem:

### My solution:

## Day 3:
### Part 1 Problem:
### My solution:
### Part 2 Problem:
### My solution:

## Day 4:
### Part 1 Problem:
### My solution:
### Part 2 Problem:
### My solution:

## Day 5:
### Part 1 Problem:
### My solution:
### Part 2 Problem:
### My solution:

## Day 6:
### Part 1 Problem:
### My solution:
### Part 2 Problem:
### My solution:

## Day 7:
### Part 1 Problem:
### My solution:
### Part 2 Problem:
### My solution:

## Day 8:
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
