def multiples(n, high):
    for i in range(1, high + 1):
        print(n * high, end="   ")
    print()


def print_table(high):
    for i in range(1, high + 1):
        multiples(i, high)


print_table(7)
