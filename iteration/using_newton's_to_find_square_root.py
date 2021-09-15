def sqrt(n):
    approx = n / 2.0
    while True:
        better_num: float = (approx + n / approx) / 2.0
        if (approx - better_num) < 0.001:
            return better_num
        else:
            approx = better_num


print(sqrt(25))
