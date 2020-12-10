# 2 pointer search for 2 numbers that search to curr_num
# O(nlogn) to sort, O(n) to find nums = O(nlogn)
def search_sum(prev_nums, curr_num):
    sorted_nums = list(sorted(prev_nums.keys()))
    l = 0
    r = len(sorted_nums) - 1
    while l < r and sorted_nums[l] + sorted_nums[r] != curr_num:
        if sorted_nums[r] > curr_num:
            r -= 1
        elif sorted_nums[l] + sorted_nums[r] < curr_num:
            l += 1
        elif sorted_nums[l] + sorted_nums[r] > curr_num:
            r -= 1
    return sorted_nums[l] + sorted_nums[r] == curr_num and l != r


# O(n) amortized search for compliment.
def search_sum_fast(prev_nums, curr_num):
    for k in prev_nums.keys():
        if curr_num - k in prev_nums:
            return True
    return False


# Sliding variable-length window finds sequence of nums that sum to curr_nums
# O(n)
def find_contiguous_sequence(prev_nums, curr_num):
    l = 0
    r = 0
    total = prev_nums[0]
    while r < len(prev_nums) and total != curr_num:
        if total > curr_num:
            total -= prev_nums[l]
            l += 1
        elif total < curr_num:
            r += 1
            if r >= len(prev_nums):
                break
            total += prev_nums[r]
    return (l, r)


if __name__ == '__main__':
    filename = 'data.txt'
    with open(filename) as f:
        data = [int(x) for x in f.read().rstrip().split('\n')]

    preamble = 25
    l = 0
    r = preamble - 1
    c = preamble
    prev_25 = {}
    # Add first numbers to map
    for i in range(0, preamble):
        if data[i] not in prev_25:
            prev_25[data[i]] = 1
        else:
            prev_25[data[i]] += 1

    # Sliding window to add/remove elements in prev 25 mapping.
    # O(n) amortized * O(n) = amortized O(n^2)
    while c < len(data):
        if not search_sum_fast(prev_25, data[c]):
            print(
                f'First number for which 2 previous numbers in prev. {preamble} do not sum to {data[c]}'
            )
            break
        c += 1
        prev_25[data[l]] -= 1
        if prev_25[data[l]] == 0:
            del prev_25[data[l]]
        l += 1
        r += 1
        if data[r] not in prev_25:
            prev_25[data[r]] = 1
        else:
            prev_25[data[r]] += 1
    # Part 2 O(n)
    prev_nums = data[0:c]
    beg_end_indices = find_contiguous_sequence(prev_nums, data[c])
    subsequence = data[beg_end_indices[0]:beg_end_indices[1]]

    print(f'Encryption weakness: {min(subsequence) + max(subsequence)}')
