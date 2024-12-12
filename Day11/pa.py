import sys
from functools import cache
row = []
for line in sys.stdin:
    row = list(map(int, line.strip().split()))
def generate_descendent(n):
    if n == 0:
        return [1]
    if len(str(n)) % 2 == 0:
        limit = len(str(n))//2
        return [int(str(n)[:limit]), int(str(n)[limit:])]
    else:
        return [n*2024]
@cache
def count_descendent(n, count):
    if count == 0:
        return 1
    descendents = generate_descendent(n)
    return sum([count_descendent(e, count - 1) for e in descendents])
result1 = sum([count_descendent(e, 75) for e in row])
print(result1)