
import sys
import re

robots = []
for line in sys.stdin:
    if line == "\n":
        continue
    parts = re.split("=| ", line)
    p_0 = int(parts[1].split(",")[0])
    p_1 = int(parts[1].split(",")[1])
    v_0 = int(parts[3].strip().split(",")[0])
    v_1 = int(parts[3].strip().split(",")[1])
    
    robots.append((p_0, p_1, v_0, v_1))
    
size_x = 101
size_y = 103

def find_next_position(robot, time, size_x, size_y):
    p_0, p_1, v_0, v_1 = robot
    new_p_0 = (p_0 + time * v_0) % size_x
    new_p_1 = (p_1 + time * v_1) % size_y
    return (new_p_0, new_p_1, v_0, v_1)
def count_quadrant(robots, size_x, size_y):
    q_1, q_2, q_3, q_4 = 0, 0, 0, 0
    for robot in robots:
        if robot[0] < size_x // 2 and robot[1] < size_y // 2:
            q_1 += 1
        if robot[0] < size_x // 2 and robot[1] > size_y // 2:
            q_2 += 1
        if robot[0] > size_x // 2 and robot[1] < size_y // 2:
            q_3 += 1
        if robot[0] > size_x // 2 and robot[1] > size_y // 2:
            q_4 += 1
    return (q_1, q_2, q_3, q_4)
next_100_position = [find_next_position(robot, 100, size_x, size_y) for robot in robots]
print(count_quadrant(next_100_position, size_x, size_y))
def product(t):
    return t[0] * t[1] * t[2] * t[3]
print(product(count_quadrant(next_100_position, size_x, size_y)))
def display(robots, size_x, size_y):
    grid = [["." for _ in range(size_x)] for _ in range(size_y)]
    for robot in robots:
        if grid[robot[1]][robot[0]] == ".":
            grid[robot[1]][robot[0]] = "1"
        else:
            grid[robot[1]][robot[0]] = str(int(grid[robot[1]][robot[0]]) + 1)
    for row in grid:
        print("".join(row))
def is_all_unique(robots):
    return len(robots) == len(set((robot[0], robot[1]) for robot in robots))

count = 0
start = 0
while count < 5:
    next_100_position = [find_next_position(robot, start, size_x, size_y) for robot in robots]
    if is_all_unique(next_100_position):
        print(start)
        display(next_100_position, size_x, size_y)
        count += 1
    start += 1
    