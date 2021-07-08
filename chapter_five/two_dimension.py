a = [[1, 2, 3, 4, 5],
     [34, 59, 20, 9, 10],
     [3, 3, 4, 5, 2, 8]]

numbers = ["1,3,6,5,8", "3,4,6,4,2"]
firstNum = numbers[0].split(",")
secNum = numbers[1].split(",")

numbers.clear()
for i in firstNum:
    for j in secNum:
        if i == j:
            numbers.append(i)
print(numbers)
