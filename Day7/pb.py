import sys
import numpy as np

def test(inp, outp):
    # Length of binary string
    length = len(inp) 

    # Starting binary value as an integer
    start = 0  

    # Maximum binary value as an integer
    end = 3**length  

    # Loop through from 0 to 2^len (inclusive)
    for num in range(start, end):
        # Convert number to binary with leading zeros
        base_3_number = np.base_repr(num, base=3)
        padded_base_3_number = base_3_number.zfill(length)
        sum = 0
        for i in range(length):
            if padded_base_3_number[i] == '1':
                if i == 0:
                    sum = 1
                sum *= int(inp[i])
            elif padded_base_3_number[i] == '0':
                sum += int(inp[i])
            elif padded_base_3_number[i] == '2':
                if i == 0:
                    sum = int(inp[i])
                sum = int(str(sum) + str(inp[i]))
        if sum == outp:
            return True
    return False
count_sum = 0
for line in sys.stdin:
    row = list(line.strip().split(":"))
    inp = list(map(int, row[1].strip().split(" ")))
    outp = int(row[0])
    if test(inp, outp):
        print(f"Input: {inp}, Output: {outp}")
        count_sum += outp
print(count_sum)
