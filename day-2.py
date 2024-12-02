def is_safe(numbers):
    if len(numbers) <= 1:
        return True
    difference = numbers[1] - numbers[0]
    if abs(difference) < 1 or abs(difference) > 3:
        return False
    should_increase = difference > 0
    for i in range(1, len(numbers) - 1):
        curr_diff = numbers[i + 1] - numbers[i]
        if abs(curr_diff) < 1 or abs(curr_diff) > 3:
            return False
        if should_increase and curr_diff <= 0:
            return False
        if not should_increase and curr_diff >= 0:
            return False

    return True


def is_safe_with_dampener(numbers):
    if is_safe(numbers):
        return True

    for i in range(len(numbers)):
        test_sequence = numbers[:i] + numbers[i + 1:]
        if is_safe(test_sequence):
            return True

    return False


def part_1(levels):
    safe_count = 0
    for level in levels:
        if is_safe(level):
            safe_count += 1
    return safe_count


def part_2(levels):
    safe_count = 0
    for level in levels:
        if is_safe_with_dampener(level):
            safe_count += 1
    return safe_count


if __name__ == '__main__':
    levels = []
    with open('input.txt', 'r') as f:
        for item in f.readlines():
            levels.append([int(i) for i in item.split()])
    print(part_1(levels))
    print(part_2(levels))
