def find_xmas(matrix, coordinates):
    x = coordinates[0]
    y = coordinates[1]
    count = 0
    if x + 3 < len(matrix) and y + 3 < len(matrix[0]) and matrix[x+1][y+1] == "M" and matrix[x+2][y+2] == "A" and matrix[x+3][y+3] == "S":
        count += 1
    if x + 3 < len(matrix) and y - 3 >= 0 and matrix[x+1][y-1] == "M" and matrix[x+2][y-2] == "A" and matrix[x+3][y-3] == "S":
        count += 1
    if x - 3 >= 0 and y + 3 < len(matrix[0]) and matrix[x-1][y+1] == "M" and matrix[x-2][y+2] == "A" and matrix[x-3][y+3] == "S":
        count += 1
    if x - 3 >= 0 and y - 3 >= 0 and matrix[x-1][y-1] == "M" and matrix[x-2][y-2] == "A" and matrix[x-3][y-3] == "S":
        count += 1
    if x + 3 < len(matrix) and matrix[x+1][y] == "M" and matrix[x+2][y] == "A" and matrix[x+3][y] == "S":
        count += 1
    if x - 3 >= 0 and matrix[x-1][y] == "M" and matrix[x-2][y] == "A" and matrix[x-3][y] == "S":
        count += 1 
    if y + 3 < len(matrix[0]) and matrix[x][y+1] == "M" and matrix[x][y+2] == "A" and matrix[x][y+3] == "S":
        count += 1
    if y - 3 >= 0 and matrix[x][y-1] == "M" and matrix[x][y-2] == "A" and matrix[x][y-3] == "S":
        count += 1
    return count   


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
        if matrix[i][j] == "X":
            count_total += find_xmas(matrix, (i, j))

print(count_total)
    
