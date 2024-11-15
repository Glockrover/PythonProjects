def filter_primes(nums):
    prime_numbers = list()

    for i in nums:
        counter = 0
        for number in range(1, i + 1):
            if i % number == 0:
                counter += 1
        if counter == 2:
            prime_numbers.append(i)
    return prime_numbers

