import sys
import numpy as np
from enum import Enum
from collections import deque

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
        command += line.strip()
    else:
        
        row_lst = []
        row = list(line.strip())
        for r in row:
            if r == '@':
                row_lst.extend(['@','.'])
            elif r == '#':
                row_lst.extend(['#','#'])
            elif r == 'O':
                row_lst.extend(['[',']'])
            elif r == '.':
                row_lst.extend(['.','.'])
        matrix.append(row_lst)
lst_mat = matrix.copy()
matrix = np.array(matrix)
print(matrix)
print(command)

def get_box_in_direction_horizontal(matrix, x, y, direction):
    s = set()
    affected = set()
    while matrix[x, y] in ['[', ']']:
        prev_x, prev_y = x, y
        x, y = x + direction.value[0], y + direction.value[1]
        s.add((x, y, matrix[prev_x, prev_y]))
        affected.add((prev_x, prev_y, matrix[prev_x, prev_y]))
    if matrix[x, y] == '#':
        return (), ()
    return s, affected

def get_full_box(matrix, x, y):
    if matrix[x, y] == '[':
        start = [(x, y, '['), (x, y+1, ']')]
    elif matrix[x, y] == ']':
        start = [(x, y-1, '['), (x, y, ']')]
    return start

def get_neighbours(matrix, x, y, direction):
    neighbours = []
    if direction == Direction.UP:
        if matrix[x, y] == '[' and x - 1 >= 0:
            if matrix[x-1, y] == '[':
                neighbours.extend(get_full_box(matrix, x-1, y))
            if matrix[x-1, y] == ']':
                neighbours.extend(get_full_box(matrix, x-1, y))
            if matrix[x-1, y+1] == '[':
                neighbours.extend(get_full_box(matrix, x-1, y+1))
            if matrix[x-1, y] == '#' or matrix[x-1, y+1] == '#':
                return False
    elif direction == Direction.DOWN:
        if matrix[x, y] == '[' and x + 1 < matrix.shape[0]:
            if matrix[x+1, y] == '[':
                neighbours.extend(get_full_box(matrix, x+1, y))
            if matrix[x+1, y] == ']':
                neighbours.extend(get_full_box(matrix, x+1, y))
            if matrix[x+1, y+1] == '[':
                neighbours.extend(get_full_box(matrix, x+1, y+1))
            if matrix[x+1, y] == '#' or matrix[x+1, y+1] == '#':
                return False
    return neighbours

def bfs(x, y, matrix, direction):
    print('start of bfs')
    visited = set()
    start = get_full_box(matrix, x, y)
    queue = deque(start)
    while queue:
        node = queue.popleft()
        print("Node: ", node)
        if node in visited:
            continue
        visited.add(node)
        neighbors = get_neighbours(matrix, node[0], node[1], direction)
        if neighbors == False:
            return set()
        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
    print("end of bfs")
    return visited


def get_box_in_direction_vertical(matrix, x, y, direction):
    print("Tracing Vertical")
    affected = bfs(x, y, matrix, direction)
    boxes = set((x + direction.value[0], y + direction.value[1], matrix[x, y]) for x, y, _ in affected)
    return boxes, affected
    
def find_alpha(matrix):
    return tuple(x[0] for x in np.where(matrix == '@'))

def print_ndarray(matrix):
    # def format_matrix(matrix):
    #     formatted = ""
    #     for row in matrix:
    #         formatted += ''.join(row) + '\n'
    #     return formatted.strip()
    # print(format_matrix(matrix))
    pass
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
        print_ndarray(matrix)
        print("_______________________________________________________________________")
        continue
    elif matrix[next_alpha] == '[' or matrix[next_alpha] == ']':
        if direction == Direction.LEFT or direction == Direction.RIGHT:
            box, affected = get_box_in_direction_horizontal(matrix, next_alpha[0], next_alpha[1], direction)
        elif direction == Direction.UP or direction == Direction.DOWN:
            box, affected = get_box_in_direction_vertical(matrix, next_alpha[0], next_alpha[1], direction)
        print("Box: ", box)
        print("Affected: ", affected)
        if len(box) == 0: # No box found
            print('Stuck at wall')
            print_ndarray(matrix)
            print("_______________________________________________________________________")
            continue
        for b in affected:
            matrix[b[0], b[1]] = '.'
        for b in box:
            print("Moving box", b, direction)
            matrix[b[0], b[1]] = b[2]
        matrix[next_alpha] = '@'
        matrix[curr_alpha] = '.'
        curr_alpha = next_alpha
    elif matrix[next_alpha] == '.':
        print("Moving alpha empty space")
        matrix[next_alpha] = '@'
        matrix[curr_alpha] = '.'
        curr_alpha = next_alpha
        
    print_ndarray(matrix)
    print("_______________________________________________________________________")
    
gps_total = 0
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if matrix[i, j] == '[':
            gps_total += i*100 + j
            
print(gps_total)