import sys
list1 = []
list2 = []
for line in sys.stdin:
    row = list(map(int, line.strip().split()))
    list1.append(row[0])
    list2.append(row[1])
    
list1.sort()
list2.sort()
print(sum([abs(x - y) for x, y in zip(list1, list2)]))