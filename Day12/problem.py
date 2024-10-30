def product_except_self(nums):
    product_list = []
    
    for i in range(len(nums)):
        counter = 1
        for number in nums:
            if nums[i] == number:
                continue
            else:
                counter *= number
        product_list.append(counter)
    if product_list == []:
        return []
    else:
        return product_list

input_list = [0, 2, 3, 4]
print(product_except_self(input_list))

        
