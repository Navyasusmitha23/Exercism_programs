def steps(n):
    if n <= 0:
       raise ValueError("Only positive integers are allowed")

    steps_count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps_count += 1

    return steps_count
