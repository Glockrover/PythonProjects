def find_pairs_with_sum(nums, target):
    pair_list = []
    sorted_pair = []
    pairs_without_duplicates = []

    for i in nums:
        for j in nums:
            pair_list.append([i,j])
    
    for pair in pair_list:
        sorted_pair.append(sorted(pair))

    for numbers in sorted_pair:
        if numbers not in pairs_without_duplicates:
            pairs_without_duplicates.append(numbers)

    numbers = [tuple(x) for x in pairs_without_duplicates if sum(x) == target]
    return numbers


input_list = [1, 3, 2, 2, 4, 0]
find_pairs_with_sum(input_list, 4)