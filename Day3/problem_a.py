import sys
def mul(str1) -> int:
    print(str1)
    value = str1[4:-1].split(',')
    return int(value[0]) * int(value[1])
value = 0
enabled = True
for line in sys.stdin:
    lastest_char = ''
    str1 = ''
    for char in line:
        if str1 == '' and char == 'm':
            str1 += char
        elif lastest_char == 'm' and char == 'u':
            str1 += char
        elif lastest_char == 'u' and char == 'l':
            str1 += char
        elif lastest_char == 'l' and char == '(':
            str1 += char
        elif lastest_char == '(' and char.isdigit():
            str1 += char
        elif char.isdigit() and str1.startswith('mul('):
            str1 += char
        elif char == ',' and str1.startswith('mul('):
            str1 += char
        elif char == ')' and str1.startswith('mul('):
            str1 += char
            value += mul(str1) if enabled else 0
            str1 = ''
            lastest_char = ''
        elif char == 'd' and str1 == '':
            str1 += char
        elif lastest_char == 'd' and char == 'o':
            str1 += char
        elif char == '(' and str1 == 'do':
            str1 += char
        elif char == ')' and str1 == 'do(':
            enabled = True
            str1 = ''
        elif char == 'n' and str1 == 'do':
            str1 += char
        elif char == "\'" and str1 == 'don':
            str1 += char
        elif char == 't' and str1 == 'don\'':
            str1 += char
        elif char == '(' and str1 == 'don\'t':
            str1 += char
        elif char == ')' and str1 == 'don\'t(':
            enabled = False
            str1 = ''
        else:
            str1 = ''
            lastest_char = ''
            continue
        lastest_char = char
        
    print(value)