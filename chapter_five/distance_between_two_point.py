import math


def calculate_distance(x1, x2, y1, y2):
    dx = x1 - x2
    dy = y1 - y2
    distance = math.sqrt(dx * dx + dy + dy)
    # result = distance ** 0.5
    # return result
    return distance


print(calculate_distance(40, 5, 3, 50))
