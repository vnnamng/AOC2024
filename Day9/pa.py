import sys
for line in sys.stdin:
    row = list(line)[:-1]
lst = []
is_file = True
id = 0
def checksum(lst):
    result = 0
    for i in range(len(lst)):
        if lst[i] != -1:
            result += i * lst[i]
    return result
for spaces in row:
    spaces = int(spaces)
    if is_file:
        lst.extend([id]*spaces)
        is_file = False
        id += 1
    else:
        lst.extend([-1]*spaces)
        is_file = True
print(lst)    
left_ptr = 0
right_ptr = len(lst) - 1
while left_ptr < right_ptr:
    print("Left: ", left_ptr, "Right: ", right_ptr)
    print("Left: ", lst[left_ptr], "Right: ", lst[right_ptr])
    if lst[left_ptr] == -1:
        if lst[right_ptr] != -1:
            lst[left_ptr], lst[right_ptr] = lst[right_ptr], lst[left_ptr]
            right_ptr -= 1
        else:
            right_ptr -= 1
            continue
    left_ptr += 1
print(checksum(lst))