def find_modes(nums):
    mode = set()
    for numbers in nums:
        if nums.count(numbers) > 1:
            mode.add(numbers)
    return list(mode)

input_list = [1, 2, 2, 3, 4]
print(find_modes(input_list))