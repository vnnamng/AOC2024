import sys
list1 = []
dict2 = {}
for line in sys.stdin:
    row = list(map(int, line.strip().split()))
    list1.append(row[0])
    if row[1] in dict2:
        dict2[row[1]] += 1
    else:
        dict2[row[1]] = 1
print(sum([x * dict2.get(x, 0) for x in list1]))