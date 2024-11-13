def max_subarray_sum(nums):
    if nums == []:
        return 0
    
    bigest = 0
    ListOfList = []

    for i in range(len(nums)):
        for j in range(len(nums) + 1):
            ListOfList.append(nums[i: j])
    
    for array in ListOfList:
        if sum(array) > bigest:
            bigest = sum(array)

    if bigest > 0:
        return bigest
    else:
        return max(nums)

print(max_subarray_sum([-3, -1, -2]))