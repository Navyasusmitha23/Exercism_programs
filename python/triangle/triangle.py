def equilateral(sides):
    a, b, c = sides
    if a == b == c and a != 0:
        return True
    return False

def isosceles(sides):
    a, b, c = sides
    if a != 0 and b != 0 and c != 0:
        if a + b >= c and b + c >= a and c + a >= b:
            if a == b or b == c or c == a:
                return True
    return False

def scalene(sides):
    a, b, c = sides
    if a != 0 and b != 0 and c != 0:
        if a + b > c and b + c > a and c + a > b:
            if a != b and b != c and a != c:
                return True
    return False
