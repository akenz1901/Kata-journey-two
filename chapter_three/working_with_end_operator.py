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
        continue
    print(i)

num = int(input("enter number: "))
while True:
    three_seq_one(num)
    response = input("Do you want to perform another task? ").lower()
    if response != "yes":
        break
    else:
        raise ValueError("Wrong Input")

celeb = [("michael", 1995), ("mercy", 1995), ("Elizabeth", 1999)]

for (name, year) in celeb:
    print(name, end=", ")
    print(year, end=".\n")

students = [('amaka', ['com sci', 'economics']),
            ('shile', ['Software Eng', 'design']),
            ('nne', ['com sci', 'data science']),
            ('toheeb', ['com sci', 'economics', 'english']),
            ('chinedu', ['com sci', 'economics', 'mathematics'])]
for name, course in students:
    print(name, "takes", len(course), "course", end=".\n")
