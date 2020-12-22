def part1(seats):
    coordinates = [(k, l) for k in range(-1, 2) for l in range(-1,2) if k != 0 or l != 0]
    for x in range(1, 100):
        copy = []
        for row in seats:
            copy_row = []
            for char in row:
                copy_row.append(char)
            copy.append(copy_row)
        for i in range(len(seats)):
            for j in range(len(seats[i])):
                if seats[i][j] == '.':
                    continue
                num_occ = 0
                for coordinate in coordinates:
                     
                    if 0 <= i + coordinate[0] < len(seats) and 0 <= j + coordinate[1] < len(seats[i]):
                        if seats[i + coordinate[0]][j + coordinate[1]] == '#':
                            num_occ += 1
                if seats[i][j] == '#' and num_occ >=4:
                    copy[i][j] = 'L'
                elif seats[i][j] == 'L' and num_occ == 0:
                    copy[i][j] = '#'
                else:
                    copy[i][j] = seats[i][j]
        if seats == copy:
            break
        seats = copy
    num_occ = 0
    for row in seats:
        for char in row:
            if char == '#':
                    num_occ += 1
    print(num_occ)

# Will return to part2.. it's annoying to debug.
def part2(seats):
    for _ in range(1, 6):
        for row in seats:
            print(''.join(row))
        print('---------------')
        coordinates = [(k, l) for k in range(-1, 2) for l in range(-1,2) if k != 0 or l != 0]
        copy = []
        for row in seats:
            copy_row = []
            for char in row:
                copy_row.append(char)
            copy.append(copy_row)
        for i in range(len(seats)):
            for j in range(len(seats[i])):
                if seats[i][j] == '.':
                    continue
                num_occ = 0
                for coord in coordinates:
                    x = coord[0]
                    y = coord[1]
                    found = False
                    while 0 <= i + x < len(seats) and 0 <= j + y < len(seats[i]) and not found:
                        if seats[i + x][j + y] == '#':
                            num_occ += 1
                            break
                        if seats[i + x][j + y] == 'L':
                            break
                        if x != 0:
                            x += 1
                        if y != 0:
                            y += 1
                if seats[i][j] == '#' and num_occ >= 5:
                    copy[i][j] = 'L'
                elif seats[i][j] == 'L' and num_occ == 0:
                    copy[i][j] = '#'
                else:
                    copy[i][j] = seats[i][j]
        for row in copy:
            print(''.join(row))
        print('-----------------')




if __name__ == '__main__':
    filename = 'test.txt'
    with open(filename) as f:
        lines = f.read().rstrip().split()
    part2(lines)
