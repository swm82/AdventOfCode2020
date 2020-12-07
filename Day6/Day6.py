def get_responses(group_responses):
    unique_responses = set()
    for response in group_responses:
        # add chars in string (as char array) to set to remove duplicates
        unique_responses.update(list(response))
    return unique_responses


if __name__ == '__main__':
    group_info = []
    filename = 'data.txt'
    with open(filename) as f:
        # split into groups, split groups into individuals
        group_info = [x.split('\n') for x in f.read().rstrip().split('\n\n')]
    total = 0
    print(group_info)
    print(f'Sum of group responses: ', end='')
    for group in group_info:
        total += len(get_responses(group))
    print(total)

    total = 0
    print(f'sum of group consolidated responses: ', end='')
    for group in group_info:
        # Get responses of first individual in group
        combined_responses = get_responses(group[0])
        # Find intersection of each individual's response set
        for response in group[1:]:
            combined_responses = combined_responses.intersection(get_responses(response))
        total += len(combined_responses)
    print(total)