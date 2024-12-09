import sys
import heapq
from sortedcontainers import SortedSet

for line in sys.stdin:
    row = list(line)[:-1]
lst = []
is_file = True
id = 0
spaces_set = set()
file_dict = {}
def checksum(lst):
    result = 0
    for i in range(len(lst)):
        if lst[i] != -1:
            result += i * lst[i]
    return result
for spaces in row:
    spaces = int(spaces)
    if is_file:
        file_dict[id] = (spaces, len(lst))
        lst.extend([id]*spaces)
        is_file = False
        id += 1
    else:
        spaces_set.add((spaces, len(lst)))
        lst.extend([-1]*spaces)
        is_file = True
def get_partition(spaces_set, starting_id, space):
    candidates = [pair for pair in spaces_set if pair[1] < starting_id and pair[0] >= space]
    if len(candidates) == 0:
        return None
    return min(candidates, key=lambda x: x[1])
for i in range(id-1, -1, -1):
    spaces_to_remove, start_index = file_dict[i]
    partition = get_partition(spaces_set, start_index, spaces_to_remove)
    print(partition)
    if partition is not None:
        spaces_set.remove((partition[0], partition[1]))
        if partition[0] > spaces_to_remove:
            spaces_set.add((partition[0] - spaces_to_remove, partition[1] + spaces_to_remove))
        for j in range(partition[1], partition[1] + spaces_to_remove):
            lst[j] = i
        for i in range(start_index, start_index + spaces_to_remove):
            lst[i] = -1
print(lst)
print(checksum(lst))

