def removeDuplicate():
    numbers = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]

    insert = 0
    for i in numbers:
        if insert <= 5:
            numbers.append(insert)
            insert += 1
        elif insert > 5:
            numbers.remove(i)
            insert += 1
    return numbers


print(removeDuplicate())
