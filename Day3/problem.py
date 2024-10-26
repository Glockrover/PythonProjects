def remove_duplicates(nums):
    new_list = []
    for i in nums:
        if i not in new_list:
            new_list.append(i)
        else:
            continue
    return new_list


