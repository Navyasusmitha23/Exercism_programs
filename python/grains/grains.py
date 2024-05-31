def square(number):
    if number not in range(1,65):
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)

def total():
    a = 0
    for i in range(1,65):
        a += square(i)
    return a