import random


def calculate_randomly():
    number = random.Random()

    roll_a_dice = number.randrange(1, 10)
    delay_dice_for_seconds = number.random() * 5.0
    return roll_a_dice, delay_dice_for_seconds


def take_random_bound(num, first_bound, second_bound):
    rang = random.Random()

    result = []
    for i in range(num):
        result.append(rang.randrange(first_bound, second_bound))
    return result


print(calculate_randomly())
print(take_random_bound(4, 21, 34))
