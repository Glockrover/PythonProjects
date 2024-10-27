def filter_primes(nums):
    primes = []
    numbers = []

    for number in nums:
        for i in range(1, number + 1):
            if number % i == 0:
                numbers.append(number)
    
    for prime in numbers:
        if numbers.count(prime) == 2 and prime not in primes:
            primes.append(prime)
    
    return primes

input_list = [11, 13, 17, 19]
print(filter_primes(input_list))