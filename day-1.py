def part_1(list_1, list_2):
    sorted_list_1 = sorted(list_1)
    sorted_list_2 = sorted(list_2)
    dist = 0
    for i1, i2 in zip(sorted_list_1, sorted_list_2):
        dist += abs(i1 - i2)
    return dist


def find_first(list_2, num):
    start, end = 0, len(list_2) - 1
    while start <= end:
        mid = (start + end) // 2
        if num <= list_2[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return start


def find_last(list_2, num):
    start, end = 0, len(list_2) - 1
    while start <= end:
        mid = (start + end) // 2
        if num >= list_2[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return end


def part_2(list_1, list_2):
    sorted_list_2 = sorted(list_2)
    sim_score = 0
    for i in set(list_1):
        index_1 = find_first(sorted_list_2, i)
        if index_1 < len(sorted_list_2) and sorted_list_2[index_1] == i:
            index_2 = find_last(sorted_list_2, i)
            freq = index_2 - index_1 + 1
            sim_score += freq * i

    return sim_score


if __name__ == '__main__':
    l1 = []
    l2 = []
    with open('input.txt', 'r') as f:
        for item in f.readlines():
            i1, i2 = item.split()
            l1.append(int(i1))
            l2.append(int(i2))

    print(part_2(l1, l2))
