import sys
import numpy as np
from enum import Enum

class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

matrix = []
command = ""
is_command = False
for line in sys.stdin:
    if line == '\n':
        is_command = True
        continue
    
    if is_command:
        command += line
    else:
        row = list(line.strip())
        matrix.append(row)
lst_mat = matrix.copy()
matrix = np.array(matrix)
print(matrix)
print(command)


def get_box_in_direction(matrix, x, y, direction):
    lst = []
    while matrix[x, y] == 'O':
        x, y = x + direction.value[0], y + direction.value[1]
        lst.append((x, y))
        
    if matrix[x, y] == '#':
        return []
    return lst
    

def find_alpha(matrix):
    return tuple(x[0] for x in np.where(matrix == '@'))

curr_alpha = find_alpha(matrix)

for c in command:
    print("Command: ", c)
    if c == '<':
        direction = Direction.LEFT
    if c == '>':
        direction = Direction.RIGHT
    if c == '^':
        direction = Direction.UP
    if c == 'v':
        direction = Direction.DOWN
    
    next_alpha = curr_alpha[0] + direction.value[0], curr_alpha[1] + direction.value[1]
    if matrix[next_alpha] == '#':
        print(matrix)
        print("_______________________________________________________________________")
        continue
    elif matrix[next_alpha] == 'O':
        box = get_box_in_direction(matrix, next_alpha[0], next_alpha[1], direction)
        if box == []:
            print(matrix)
            print("_______________________________________________________________________")
            continue
        matrix[next_alpha] = '@'
        matrix[curr_alpha] = '.'
        for b in box:
            matrix[b] = 'O'
        curr_alpha = next_alpha
    elif matrix[next_alpha] == '.':
        print("Moving alpha empty space")
        matrix[next_alpha] = '@'
        matrix[curr_alpha] = '.'
        curr_alpha = next_alpha
        
    print(matrix)
    print("_______________________________________________________________________")
count_boxes = 0
count_b = 0
gps_total = 0
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if matrix[i, j] == 'O':
            count_boxes += 1
            gps_total += i*100 + j
        if lst_mat[i][j] == 'O':
            count_b += 1
        
print(gps_total)
print(len(lst_mat), len(lst_mat[0]))
print(matrix.shape)

