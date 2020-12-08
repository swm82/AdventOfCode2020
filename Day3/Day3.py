def find_trees(slope_x, slope_y, rows):
    row_length = len(rows[0])
    i = 0
    count = 0
    for r in range(0, len(rows), slope_y):
        i = i % row_length
        if rows[r][i] == '#':
            count += 1
        i += slope_x
    return count


if __name__ == '__main__':
    data = []
    with open('day3.txt') as f:
        for line in f:
            data.append(line.rstrip())

    print(f'Part 1: {find_trees(3, 1, data)}')

    print('Part 2: ', end='')
    product = 1
    for slope in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
        product *= find_trees(slope[0], slope[1], data)
    print(product)



