fail = 0
passes = 0


answer = 0


for i in range(10):
    answer = int(input("Enter either 1 for failure or 2 for pass: "))

    while answer > 2 | answer == 0:
        print("Pls Enter a correct integer")
        answer = int(input("Enter either 1 for failure or 2 for pass: "))

    if answer == 1:
        fail += 1

    else:
        passes += 1

print("how many students failed in Jss1 ", fail)
print("how many students passed in Jss1 ", passes)
