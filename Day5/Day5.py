import re

def bin_search(string, lo, hi, lo_flag, hi_flag):
    l = lo
    r = hi
    i = 0
    while l < r:
        direction = string[i]
        #print(direction + ':')
        mid = (l + r) // 2
        #print(f'Before: L: {l} - R: {r} - Char: {string[i]} Mid: {mid}')
        #print(f'{string[i]} - {mid}')
        if direction == lo_flag:
            r = mid
        elif direction == hi_flag:
            l = mid + 1
        i += 1
        #print(f'After: L: {l} - R: {r} - Char: Mid: {mid}')
    return l if direction == lo_flag else r

if __name__ == '__main__':
    filename = 'day5.txt'
    max_seat_id = 0
    min_seat_id = float('inf')
    with open(filename) as f:
        s = set()
        for line in f:
            string = line.rstrip()
            if not re.match('^(F|B){7}(L|R){3}$', string):
                continue
            row = bin_search(string[:7], 0, 127, 'F', 'B')
            col = bin_search(string[7:], 0, 7, 'L', 'R')
            seat_id = row * 8 + col
            s.add(seat_id)
            if seat_id > max_seat_id:
                max_seat_id = seat_id
            if seat_id < min_seat_id:
                min_seat_id = seat_id
        print(f'Highest seat ID: {max_seat_id}')
        # Part2: find missing id in list of seat ids
        for i in range(min_seat_id, max_seat_id + 1):
            if i not in s:
                print(f'Your seat is: {i}')
                break

