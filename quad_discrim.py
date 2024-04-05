import random


def variables():
    a = random.randint(-100, 100)
    b = random.randint(-100, 100)
    c = random.randint(-100, 100)
    if a == 0:
        a+=1
    else:
        return a, b, c


def discriminant(a, b, c):
    return (b ** 2) - (4 * a * c)


def quadratic(a, b, c):
    if discriminant(a, b, c) > 0:
        x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        return x1, x2
    elif discriminant(a, b, c) == 0:
        x = -b / (2 * a)
        return x
    # else:
    #     return None



