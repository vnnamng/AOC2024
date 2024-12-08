import sys
import numpy as np
from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

def turn(direction):
    if direction == Direction.UP:
        return Direction.RIGHT
    elif direction == Direction.RIGHT:
        return Direction.DOWN
    elif direction == Direction.DOWN:
        return Direction.LEFT
    elif direction == Direction.LEFT:
        return Direction.UP
def inbound(position, size):
    return position[0] >= 0 and position[0] < size[0] and position[1] >= 0 and position[1] < size[1]

def move(position, direction):
    if direction == Direction.UP:
        return (position[0] - 1, position[1])
    elif direction == Direction.DOWN:
        return (position[0] + 1, position[1])
    elif direction == Direction.LEFT:
        return (position[0], position[1] - 1)
    elif direction == Direction.RIGHT:
        return (position[0], position[1] + 1)

def check(position, direction, matrix):
    try:
        if direction == Direction.UP:
            return matrix[position[0] - 1, position[1]]
        elif direction == Direction.DOWN:
            return matrix[position[0] + 1, position[1]]
        elif direction == Direction.LEFT:
            return matrix[position[0], position[1] - 1]
        elif direction == Direction.RIGHT:
            return matrix[position[0], position[1] + 1]
    except IndexError:
        return False
matrix = []
start = None
for line in sys.stdin:
    row = list(line)[:-1]
    matrix.append(row)

np_matrix = np.array(matrix)

size = np_matrix.shape
start = np.where(np_matrix == "^")

direction = Direction.UP
count = 1
position = (start[0][0], start[1][0])
while check(position, direction, np_matrix):
    next_symbol = check(position, direction, np_matrix)
    if next_symbol == "#":
        direction = turn(direction)
    elif next_symbol == ".":
        count += 1
        position = move(position, direction)
        np_matrix[position[0], position[1]] = "X"
    elif next_symbol == "X":
        position = move(position, direction)
    elif next_symbol == "^":
        position = move(position, direction)
        np_matrix[position[0], position[1]] = "X"

np.printoptions(threshold=np.inf)
print(np_matrix)
print(count)



