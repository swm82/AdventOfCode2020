def forward(position, value):
    if position[2] == 'n':
        position[1] += value
    elif position[2] == 's':
        position[1] -= value
    elif position[2] == 'e':
        position[0] += value
    else:
        position[0] -= value

# Decomposes the degree of rotation into number of 90* turns.
# Number is applied to current direction (represented as an integer) and moded by 4 keep
# within N,S,E,W directions
def change_direction(position, orientation, value):
    direction_array = ['n', 'e', 's', 'w']
    direction_dict = {'n': 0, 'e': 1, 's': 2, 'w': 3}
    turns = value // 90
    curr_dir_value = direction_dict[position[2]]
    curr_dir_value = curr_dir_value + turns if orientation == 'R' else curr_dir_value - turns
    new_dir_value = curr_dir_value % 4
    position[2] = direction_array[new_dir_value]

def handle_instruction(position, instruction):
    value = instruction[1]
    orientation = instruction[0]
    if orientation == 'F':
        forward(position, instruction[1])
    elif orientation == 'N':
        position[1] += value
    elif orientation == 'S':
        position[1] -= value
    elif orientation == 'E':
        position[0] += value
    elif orientation == 'W':
        position[0] -= value
    elif orientation in ['L', 'R']:
        change_direction(position, orientation, value)


if __name__ == '__main__':
    filename = 'data.txt'
    with open(filename) as f:
        directions = [(x[0], int(x[1:])) for x in f.read().rstrip().split()]

    position = [0, 0, 'e']
    for instruction in directions:
        handle_instruction(position, instruction)
    print(f'Manhattan distance from starting location: {abs(position[0]) + abs(position[1])}')
