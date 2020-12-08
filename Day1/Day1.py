data = set()
with open ("day1.txt") as f:
    for line in f:
        data.add(int(line.strip()))

def pt1():
    for val in data:
        diff = 2020 - val
        if diff in data:
            return val * diff


def pt2():
    for val1 in data:
        for val2 in data:
            diff = 2020 - val1 - val2
            if diff in data:
                return val1 * val2 * diff

print(f'Part1 solution: {pt1()}')
print(f'Part2 solution: {pt2()}')

