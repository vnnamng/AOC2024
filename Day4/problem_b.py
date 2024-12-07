def find_xmas(matrix, coordinates):
    x = coordinates[0]
    y = coordinates[1]
    if x + 1 < len(matrix) and x - 1 >= 0 and y + 1 < len(matrix[0]) and y - 1 >= 0:
        if matrix[x+1][y+1] == "M" and matrix[x-1][y+1] == "S" and matrix[x+1][y-1] == "M" and matrix[x-1][y-1] == "S":
            
            return 1
        if matrix[x+1][y+1] == "M" and matrix[x-1][y+1] == "M" and matrix[x+1][y-1] == "S" and matrix[x-1][y-1] == "S":
            
            return 1
        if matrix[x+1][y+1] == "S" and matrix[x-1][y+1] == "M" and matrix[x+1][y-1] == "S" and matrix[x-1][y-1] == "M":
            
            return 1
        if matrix[x+1][y+1] == "S" and matrix[x-1][y+1] == "S" and matrix[x+1][y-1] == "M" and matrix[x-1][y-1] == "M":
            
            return 1
    return 0   


import sys
matrix = []
for line in sys.stdin:
    new_row = []
    for char in line:
        new_row.append(char)
    matrix.append(new_row)
count_total = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == "A":
            count_total += find_xmas(matrix, (i, j))

print(count_total)