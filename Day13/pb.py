# find min 3x + y
# given 
# a_1x + a_2y = p1
# b_1x + b_2y = p2

from scipy.optimize import linprog





def solve_LP(A_eq, b_eq):
#     A_eq = [[26, 67], [66, 21]]
#     b_eq = [10000000012748, 10000000012176]

    # Define the problem
    # A_eq = [[94, 22], [34, 67]]
    # b_eq = [10000000008400, 10000000005400]

    # Bounds for x1 and x2 (nonnegative)
    bounds = [(0, None), (0, None)]

    # Use linprog for integer-like constraints
    res = linprog(c=[3, 1], A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

    # Check if solution is valid
    if not res.success:
        return None
    x_1, x_2 = res.x
    x_1 = round(x_1)
    x_2 = round(x_2)
    if A_eq[0][0]*x_1 + A_eq[0][1]*x_2 == b_eq[0] and A_eq[1][0]*x_1 + A_eq[1][1]*x_2 == b_eq[1]:
        return (x_1, x_2)
    else:
        return None

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
        x_value = int(parts[0].split("=")[1]) + 10000000000000
        y_value = int(parts[1].split("=")[1]) + 10000000000000
        curr.append((x_value, y_value))
        lst.append(curr)
        curr = []
count = 0    
for eq in lst:
    print(eq)
    # val = find_min((eq[0][0], eq[1][0]), (eq[0][1], eq[1][1]), eq[2])
    # if val < float('inf'):
        # count += val
    result = solve_LP([(eq[0][0], eq[1][0]), (eq[0][1], eq[1][1])], eq[2])
    print(result)
    if result is not None:
        print(3 * result[0] + result[1])
        count += 3 * result[0] + result[1]
print(count)