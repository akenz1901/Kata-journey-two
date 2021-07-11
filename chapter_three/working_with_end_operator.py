def three_seq_one(number):
    while number != 1:
        print(number, end=", ")
        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1
    print(number, end=".\n")


three_seq_one(3)

for i in range(10):
    print(i, "\t", 2**i)

for i in range(1, 7):
    print(i+2, end="   ")

for i in [12, 4, 5, 9, 23]:
    if i % 2 == 1:
        break
    print(i)
