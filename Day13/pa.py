# find min 3x + y
# given 
# a_1x + a_2y = p1
# b_1x + b_2y = p2

def find_min(a, b, p):
    a_1 = a[0]
    a_2 = a[1]
    b_1 = b[0]
    b_2 = b[1]
    p1 = p[0]
    p2 = p[1]
    curr_min = float('inf')
    for x in range (0, p1 // a_1 + 1):
        if p1 - a_1*x >= 0 and (p1 - a_1*x) % a_2 == 0:
            y = (p1 - a_1*x) // a_2
            if p2 - b_1*x >= 0 and (p2 - b_1*x) % b_2 == 0:
                y2 = (p2 - b_1*x) // b_2
                if y == y2:
                    curr_min = min(curr_min, 3*x + y)
    return curr_min

lst = []
curr = []
import sys
for line in sys.stdin:
    if line == "\n":
        continue
    parts = line.split(", ")
    if line.startswith("Button"):
        x_value = int(parts[0].split("+")[1])
        y_value = int(parts[1].split("+")[1])
        curr.append((x_value, y_value))
    if line.startswith("Prize"):
        x_value = int(parts[0].split("=")[1]) 
        y_value = int(parts[1].split("=")[1]) 
        curr.append((x_value, y_value))
        lst.append(curr)
        curr = []
count = 0    
for eq in lst:
    print(eq)
    val = find_min((eq[0][0], eq[1][0]), (eq[0][1], eq[1][1]), eq[2])
    print(val)
    if val < float('inf'):
        count += val
        
print(count)