def find_modes(nums):
    mode1 = []
    mode = []
    for i in range(len(nums)):
        if nums[i] not in mode:
            mode.append(nums[i])
        else:
            mode1.append(nums[i])

    if mode == mode1:
        return mode
    else:
        return mode1

