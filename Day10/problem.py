def factorial(n):
    if n == 1:
        return 1
    elif n < 0:
        raise ValueError
    else:
        counter = 1
        for i in range(n , 1, -1):
            counter *= i
        return counter
