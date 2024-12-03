import re
from dataclasses import dataclass
from typing import Tuple


@dataclass
class Instruction:
    type: str
    position: int
    numbers: Tuple[int, int] = None


def find_all_instructions(memory):
    instructions = []
    for match in re.finditer(r'mul\((\d+),(\d+)\)', memory):
        instructions.append(Instruction(
            type='mul',
            position=match.start(),
            numbers=(int(match.group(1)), int(match.group(2)))
        ))

    for match in re.finditer(r'do\(\)', memory):
        instructions.append(Instruction(
            type='do',
            position=match.start()
        ))

    for match in re.finditer(r"don't\(\)", memory):
        instructions.append(Instruction(
            type='dont',
            position=match.start()
        ))

    return sorted(instructions, key=lambda x: x.position)


def part_2(content):
    instructions = find_all_instructions(content)
    mul_enabled = True
    total = 0

    for instruction in instructions:
        if instruction.type == 'do':
            mul_enabled = True
            print(f"Position {instruction.position}: Enabling multiplications")
        elif instruction.type == 'dont':
            mul_enabled = False
            print(f"Position {instruction.position}: Disabling multiplications")
        elif instruction.type == 'mul' and mul_enabled:
            x, y = instruction.numbers
            result = x * y
            total += result
            print(f"Position {instruction.position}: mul({x},{y}) = {result} (enabled)")
        elif instruction.type == 'mul':
            x, y = instruction.numbers
            print(f"Position {instruction.position}: mul({x},{y}) (disabled)")

    return total


def part_1(content):
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.finditer(pattern, content)

    total = 0
    for match in matches:
        x = int(match.group(1))
        y = int(match.group(2))
        result = x * y
        total += result
        print(f"Found mul({x},{y}) = {result}")

    return total


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        content = f.read()
        print(part_1("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"))
        print(part_1(content))
        print(part_2(content))