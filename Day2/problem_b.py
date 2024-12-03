import sys
def is_safe(row: list[int]) -> bool:
    delta = 0
    for i in range(1, len(row)):
        if row[i] - row[i - 1] == 0:
            return False
        elif -3 <= row[i] - row[i - 1] <= 3:
            if delta * (row[i] - row[i - 1]) < 0:
                return False
            delta = row[i] - row[i - 1]
        else:
            return False
    return True

def is_safe_reduced(row: list[int]) -> bool:
    print(row)
    if is_safe(row):
        print("Safe")
        return True
    else:
        for i in range(len(row)):
            if is_safe(row[:i] + row[i+1:]):
                print("Removed at index", i)
                return True
        print("Not safe")
        return False
    
count = 0
for line in sys.stdin:
    row = list(map(int, line.strip().split()))
    count += 1 if is_safe_reduced(row) else 0
print(count)
