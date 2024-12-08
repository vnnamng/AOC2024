import sys
matrix = []
for line in sys.stdin:
    row = list(line)[:-1]
    matrix.append(row)
    
attenna_map = {}
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
        if matrix[i][j] != '.':
            if matrix[i][j] not in attenna_map:
                attenna_map[matrix[i][j]] = []
            attenna_map[matrix[i][j]].append((i, j))

def generate_antinode(attenna_lst, size_x, size_y):
    antinode_set = set()
    for i in range(0, len(attenna_lst)):
        for j in range(i+1, len(attenna_lst)):
            x1, y1 = attenna_lst[i]
            x2, y2 = attenna_lst[j]
            antinode_1 = (2*x1 - x2, 2*y1 - y2)
            antinode_2 = (2*x2 - x1, 2*y2 - y1)
            if 0 <= antinode_1[0] < size_x and 0 <= antinode_1[1] < size_y:
                antinode_set.add(antinode_1)
            if 0 <= antinode_2[0] < size_x and 0 <= antinode_2[1] < size_y:
                antinode_set.add(antinode_2)
    return antinode_set


output_set = set()
for key in attenna_map:
    antinode_set = generate_antinode(attenna_map[key], len(matrix), len(matrix[0]))
    output_set = output_set.union(antinode_set)
    
print((output_set)) 
print(len(output_set))