def big_and_small(numbers):
    big = max(numbers)
    small = min(numbers)
    return f"{big} is the Biggest and {small} is the smallest."


random_numbers = [2, 5, 9, 10, 20, 400, 33, 11, 100]
print(big_and_small(random_numbers))