def most_frequent(nums):
    dict_nums = {x : nums.count(x) for x in nums}
    
    counter = 0
    for key, value in dict_nums.items():
        if value > counter:
            counter = key
    
    if nums != []:
        return counter
        


print(most_frequent([]))