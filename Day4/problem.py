def fibonacci(n):
    if n >= 0:
        numbers = []
        f1 = 0
        f2 = 1
        numbers.append(f1)
        numbers.append(f2)
        while True:
            f3 = f1 + f2
            f1 = f2
            f2 = f3
            numbers.append(f3)
            if len(numbers) > n:
                break
        return numbers[n]
    else:
        raise ValueError

print(fibonacci(10))