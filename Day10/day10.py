# O(nlogn) to sort + O(n) to evaulate = O(nlogn)
def part_1(adapter_list):
    num_1 = 0
    num_3 = 0
    prev = 0
    for adapter in adapters:
        if adapter - prev == 1:
            num_1 += 1
        elif adapter - prev == 3:
            num_3 += 1
        prev = adapter
    return num_1 * num_3


# Driver method for permutations
def part_2(adapter_list):
    memo = [0 for x in adapter_list]
    return generate_permutations(adapter_list, 0, memo)


# Recursively generates configuration permutations
# Memoization (top down dynamic program) increases efficiency by saving permutations at each index,
# and reuses those values for later computations
# O(n)?
def generate_permutations(adapter_list, i, memo):
    if i >= len(adapter_list) - 1:
        return 1
    permutations = 0
    if memo[i]:
        return memo[i]
    if adapter_list[i + 1] - adapter_list[i] == 1:
        permutations += generate_permutations(adapter_list, i + 1, memo)
    for j in range(i + 1, i + 4):
        if j >= len(adapter_list):
            break
        if adapter_list[j] - adapter_list[i] in [2, 3]:
            permutations += generate_permutations(adapter_list, j, memo)
    memo[i] = permutations
    return permutations


if __name__ == '__main__':
    filename = 'data.txt'
    with open(filename) as f:
        adapters = [0]
        adapters += [int(x) for x in f.read().rstrip().split()]
    adapters.sort()
    adapters.append(adapters[len(adapters) - 1] + 3)
    print(
        f'Number of 3 jolt differences * 1 jolt differences: {part_1(adapters)}'
    )
    print(
        f'Number of distinct adapter configurations: {part_2(adapters)}'
    )
