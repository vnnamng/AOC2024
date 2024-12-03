import sys
def is_safe(row: list[int]) -> bool:
    print(row)
    delta = 0
    for i in range(1, len(row)):
        print(row[i], row[i - 1])
        if row[i] - row[i - 1] == 0:
            return False
        elif -3 <= row[i] - row[i - 1] <= 3:
            if delta * (row[i] - row[i - 1]) < 0:
                return False
            delta = row[i] - row[i - 1]
        else:
            return False
    return True
        
count = 0
for line in sys.stdin:
    row = list(map(int, line.strip().split()))
    count += 1 if is_safe(row) else 0
print(count)
