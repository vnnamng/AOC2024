import sys
from collections import deque
from enum import Enum

matrix = []
for line in sys.stdin:
    row = list(line)[:-1]
    matrix.append(row)

# fence = (x1, y1, x2, y2, region_1, region_2)
# out of bound, x1 = -1 or x2 = len(matrix), y1 = -1 or y2 = len(matrix[0])
fences = set()

def label_regions(matrix):
    def flood_fill(i, j, region_id):
        """Flood-fill to find all cells in the same region."""
        stack = [(i, j)]
        region = set()
        visited.add((i, j))
        target_char = matrix[i][j]

        while stack:
            x, y = stack.pop()
            region.add((x, y))

            # Check all 4 neighbors
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                    if matrix[nx][ny] == target_char:
                        visited.add((nx, ny))
                        stack.append((nx, ny))
        
        return region

    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    visited = set()
    regions = {}
    region_id = 1

    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited:  # Start a new region
                region_cells = flood_fill(i, j, region_id)
                regions[region_id] = region_cells
                region_id += 1

    return regions

region = label_regions(matrix)

for i in range(len(matrix)-1):
    for j in range(len(matrix[i])):
        if matrix[i][j] != matrix[i+1][j]:
            fences.add((i, j, i+1, j, matrix[i][j], matrix[i+1][j]))
for i in range(len(matrix)):
    for j in range(len(matrix[i])-1):
        if matrix[i][j] != matrix[i][j+1]:
            fences.add((i, j, i, j+1, matrix[i][j], matrix[i][j+1]))
            
for j in range(len(matrix[0])):
    fences.add((-1, j, 0, j, '.', matrix[0][j]))
    fences.add((len(matrix)-1, j, len(matrix), j, matrix[-1][j], '.'))

for i in range(len(matrix)):
    fences.add((i, -1, i, 0, '.', matrix[i][0]))
    fences.add((i, len(matrix[0])-1, i, len(matrix[0]), matrix[i][-1], '.'))

def count_side(matrix, fences, region, region_idx):
    return count_side_idx(matrix, fences, region, region_idx, True) + count_side_idx(matrix, fences, region, region_idx, False)

def count_side_idx(matrix, fences, region, region_idx, is_first):
    if is_first:
        lst = [e for e in fences if (e[0], e[1]) in region[region_idx]]
    else:
        lst = [e for e in fences if (e[2], e[3]) in region[region_idx]]
    x = len(matrix)
    y = len(matrix[0])
    acc = 0
    for i in range(-1, y + 1):
        horizontal_fences = ([e[1] for e in lst if e[0] == i and e[2] == i+1])
        acc += count_breaks(horizontal_fences)
    for j in range(-1, x + 1):
        vertical_fences = ([e[0] for e in lst if e[1] == j and e[3] == j+1])
        acc += count_breaks(vertical_fences)
    return acc

def count_breaks(lst):
    if lst == []:
        return 0
    lst = sorted(lst)
    count = 1
    for i in range(1,len(lst)):
        if lst[i] != lst[i-1] + 1:
            count += 1
    return count
def id_to_name(region, matrix, r):
    id = list(region[r])[0]
    return matrix[id[0]][id[1]]
# print(count_side(matrix, fences, 'A'))
print([count_side(matrix, fences, region, e) for e in region])
print([len(region[e]) for e in region])
print([id_to_name(region, matrix, e) for e in region])
print([(id_to_name(region, matrix, e), count_side(matrix, fences, region, e)*len(region[e])) for e in region])
print(sum([count_side(matrix, fences, region, e)*len(region[e]) for e in region]))
    
