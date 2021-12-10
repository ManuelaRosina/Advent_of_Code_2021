from numpy import median

points = {')':3, ']':57, '}':1197, '>':25137}
points_p2 = {')':1, ']':2, '}':3, '>':4}
closing_b = {'(':')', '[':']', '{':'}', '<':'>'}

def same_b(b1, b2):
    if b1 == '(' and b2 == ')':
        return True
    if b1 == '[' and b2 == ']':
        return True
    if b1 == '{' and b2 == '}':
        return True
    if b1 == '<' and b2 == '>':
        return True
    return False

def reverse_b(brackets):
    reversed_b = []
    brackets.reverse()
    for b in brackets:
        reversed_b.append(closing_b[b])
        
    return reversed_b

def score_part_2(brackets):
    score = 0
    for b in brackets:
        score *= 5
        score += points_p2[b]
    return score

chunks = []
with open('input_day10.txt') as f:
    for line in f:
        chunks.append(line.rstrip())

opend = []
syntax_error = 0
error_chunks = []
for i, chunk in enumerate(chunks):
    for bracket in chunk:
        if bracket in ['(', '{', '<', '[']:
            opend.append(bracket)
        else:
            if not same_b(opend[-1], bracket):
                #print('error: found ', bracket, ' expected ', opend[-1])
                syntax_error += points[bracket]
                error_chunks.append(i)
                break
            else:
                opend.pop()
print("Part 1: ", syntax_error)

incomplete_chunks = [chunk for i, chunk in enumerate(chunks) if i not in error_chunks]

open_chunks = []
scores = []
for i, chunk in enumerate(incomplete_chunks):
    opend = []
    for bracket in chunk:
        if bracket in ['(', '{', '<', '[']:
            opend.append(bracket)
        else:
            if same_b(opend[-1], bracket):
                opend.pop()
            else:
                print("ERROR") # This should not happen!!!
    closing = reverse_b(opend)
    open_chunks.append(closing)
    scores.append(score_part_2(closing))
    
print("Part 2: ", int(median(scores)))
