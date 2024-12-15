from scipy.optimize import linprog

# Define the problem
# A_eq = [[94, 22], [34, 67]]
# b_eq = [10000000008400, 10000000005400]

A_eq = [[26, 67], [66, 21]]
b_eq = [10000000012748, 10000000012176]

# Bounds for x1 and x2 (nonnegative)
bounds = [(0, None), (0, None)]

# Use linprog for integer-like constraints
res = linprog(c=[3, 1], A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

# Check if solution is valid
if res.success and all(x.is_integer() for x in res.x):
    print("Nonnegative integer solution:", tuple(map(int, res.x)))
else:
    print("No solution found or requires approximation.")
