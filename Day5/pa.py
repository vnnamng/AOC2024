import sys

value_to_set_map = dict()
sum = 0
for line in sys.stdin:
    if "|" in line:
        row = list(map(int, line.strip().split("|")))
        if row[0] not in value_to_set_map:
            value_to_set_map[row[0]] = set()
        value_to_set_map[row[0]].add(row[1])
    elif "," in line:
        row = list(map(int, line.strip().split(",")))
        valid = True
        current_set = set()
        for e in row:
            if e in value_to_set_map and len(current_set & value_to_set_map.get(e, set())) > 0:
                valid = False
                break
            current_set.add(e)
        if valid:
            sum += row[len(row)//2]
    else:
        continue
    
print(sum)