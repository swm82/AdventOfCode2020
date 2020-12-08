def handle_input(line):
    reqs, string = [x.strip() for x in line.split(':')]
    min_max_pair, char = reqs.split()
    min_count, max_count = [int(x) for x in min_max_pair.split('-')]
    return {'min': min_count, 'max': max_count, 'char': char, 'password': string}



def part1(data):
    count = data['password'].count(data['char'])
    return count >= data['min'] and count <= data['max']


def part2(data):
    return (data['password'][data['min'] - 1] == data['char'] or data['password'][data['max'] - 1] == data['char']) and data['password'][data['min'] - 1] != data['password'][data['max'] - 1]


data =[]
part1_count = 0
part2_count = 0
with open("day2.txt") as f:
    for line in f:
        data = handle_input(line)
        part1_count += 1 if part1(data) else 0
        part2_count += 1 if part2(data) else 0
print('Part 1 count: ' + str(part1_count))
print('Part 2 count: ' + str(part2_count))