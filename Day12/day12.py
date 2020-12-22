def forward(position, value):
    if position[2] == 'n':
        position[1] += value
    elif position[2] == 's':
        position[1] -= value
    elif position[2] == 'e':
        position[0] += value
    else:
        position[0] -= value


def forward_waypoint(position, waypoint):
    position[0] += waypoint[0]
    position[1] += waypoint[1]


# Decomposes the degree of rotation into number of 90* turns.
# Number is applied to current direction (represented as an integer) and moded by 4 to keep
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
    print(
        f'Manhattan distance from starting location: {abs(position[0]) + abs(position[1])}'
    )

    # Part2
    position = [0, 0]
    waypoint = [10, 1]
    for instruction in directions:
        direction = instruction[0]
        value = instruction[1]
        if direction == 'N':
            waypoint[1] += value
        elif direction == 'S':
            waypoint[1] -= value
        elif direction == 'E':
            waypoint[0] += value
        elif direction == 'W':
            waypoint[0] -= value
        elif direction in ['L', 'R']:
            num_turns = value // 90
            num_turns = num_turns % 4
            if direction == 'L':
                # This could easily be seperated into functions
                if num_turns == 1:
                    temp = waypoint[0]
                    waypoint[0] = waypoint[1] * -1
                    waypoint[1] = temp
                elif num_turns == 2:
                    waypoint[0] = waypoint[0] * -1
                    waypoint[1] = waypoint[1] * -1
                elif num_turns == 3:
                    temp = waypoint[0]
                    waypoint[0] = waypoint[1]
                    waypoint[1] = temp * -1
            if direction == 'R':
                if num_turns == 3:
                    temp = waypoint[0]
                    waypoint[0] = waypoint[1] * -1
                    waypoint[1] = temp
                elif num_turns == 2:
                    waypoint[0] = waypoint[0] * -1
                    waypoint[1] = waypoint[1] * -1
                elif num_turns == 1:
                    temp = waypoint[0]
                    waypoint[0] = waypoint[1]
                    waypoint[1] = temp * -1
        else:
            position[0] = position[0] + (value * waypoint[0])
            position[1] = position[1] + (value * waypoint[1])

    print(f'Manhattan distance: {abs(position[0]) + abs(position[1])}')
