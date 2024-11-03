def longest_zero_sum_subarray(nums):
    if nums == []:
        return list(nums)
    elif sum(nums) == 0:
        return nums
    else:
        array = []
        for number in range(len(nums)):
            for i in range(number + 1, len(nums) + 1):
                array.append(nums[number:i])
        
        new = list()
        for numbers in array:
            if sum(numbers) == 0:
                new.append(numbers)
        if new:
            return new[0]
        else:
            return []

print(longest_zero_sum_subarray([1, 2, -3, 3, -3, 3]))