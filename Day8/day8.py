# Global accumulator, set of nop/jmp indices
accumulator = 0
jmp_nop_list = []


# structure data as a list of tuples (a, b) where a = instruction type and b = associated value
def read_data(filename):
    with open(filename) as f:
        instructions = [
            (x[0], x[1])
            for x in [y.split(' ') for y in f.read().rstrip().split('\n')]
        ]
    return instructions


def handle_instruction(instruction, curr_instruction):
    global accumulator
    sign = instruction[1][0]
    amount = int(instruction[1][1:])
    instruction = instruction[0]
    if instruction == 'acc':
        accumulator = accumulator + amount if sign == '+' else accumulator - amount
        return curr_instruction + 1
    elif instruction == 'jmp':
        jmp_nop_list.append(curr_instruction)
        return curr_instruction + amount if sign == '+' else curr_instruction - amount
    else:
        jmp_nop_list.append(curr_instruction)
        return curr_instruction + 1


if __name__ == '__main__':
    filename = 'data.txt'
    instructions = read_data(filename)
    curr_instruction = 0
    past_instructions = set()
    while curr_instruction not in past_instructions:
        instruction = instructions[curr_instruction]
        past_instructions.add(curr_instruction)
        curr_instruction = handle_instruction(instruction, curr_instruction)
    print(
        f'Accumulator at the point where an instruction repeats: {accumulator}'
    )

    # Brute force apprach part2
    # For each nop/jop in list, flip the instruction, then test boot cycle for completion
    for index in jmp_nop_list:
        accumulator = 0
        found = False
        curr_instruction = 0
        past_instructions = set()
        while curr_instruction not in past_instructions:
            instruction = instructions[curr_instruction]
            # flip instruction
            if curr_instruction == index:
                if instruction[0] == 'jmp':
                    instruction = ('nop', instruction[1])
                elif instruction[0] == 'nop':
                    instruction = ('jmp', instruction[1])
            past_instructions.add(curr_instruction)
            curr_instruction = handle_instruction(instruction,
                                                  curr_instruction)
            if curr_instruction not in range(0, len(instructions)):
                found = True
                break
        if found:
            break

    print(f'Accumulator when boot completes normally: {accumulator}')
