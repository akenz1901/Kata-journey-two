import math


def return_2_values(r):
    a = 2 * math.pi * r
    b = 4 * math.e * r
    c = a + b
    return (a, b, c)  # parenthesis is redundant


return_2_values(89)
print(return_2_values(89))
