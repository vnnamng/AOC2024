import sys

value_to_set_map = dict()
sum = 0
def swap(lst, a, b):
    lst[a], lst[b] = lst[b], lst[a]
    
def is_valid(lst, value_to_set_map, idx):
    return not (lst[idx] in value_to_set_map and len(set(lst[:idx]) & value_to_set_map.get(lst[idx], set())) > 0)
for line in sys.stdin:
    if "|" in line:
        row = list(map(int, line.strip().split("|")))
        if row[0] not in value_to_set_map:
            value_to_set_map[row[0]] = set()
        value_to_set_map[row[0]].add(row[1])
    elif "," in line:
        row = list(map(int, line.strip().split(",")))
        swapped = False
        valid = True
        current_set = set()
        print(row)
        for i in range(len(row)):
            if not is_valid(row, value_to_set_map, i):
                valid = False
                break
        if valid:
            print(row)
            continue
        for i in range(len(row)):
            if is_valid(row, value_to_set_map, i):
                continue
            k = i
            while is_valid(row, value_to_set_map, k) == False:
                swapped = True
                swap(row, k, k-1)
                k -= 1
        print(row)
        sum += row[len(row)//2]
    else:
        continue
print(sum)