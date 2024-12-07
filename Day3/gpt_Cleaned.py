import sys
import re

def parse_and_calculate(expression: str) -> int:
    """
    Parse the mul() expression and calculate the result.
    Example: "mul(2,3)" -> 2 * 3 = 6
    """
    match = re.match(r"mul\((\d+),(\d+)\)", expression)
    if match:
        num1, num2 = map(int, match.groups())
        return num1 * num2
    return 0

def process_line(line: str, enabled: bool, value: int) -> (bool, int):
    """
    Process a single line of input. Adjust 'enabled' state and update 'value' based on commands.
    """
    # Find all valid commands
    commands = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line)
    
    for command in commands:
        if command == "do()":
            enabled = True
        elif command == "don't()":
            enabled = False
        elif command.startswith("mul(") and enabled:
            value += parse_and_calculate(command)
    
    return enabled, value

def main():
    value = 0
    enabled = True

    for line in sys.stdin:
        enabled, value = process_line(line.strip(), enabled, value)
        print(value)

if __name__ == "__main__":
    main()
