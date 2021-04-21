class time_properties:

    def __init__(self, hour, minute, second):
        self.hour = 0
        self.minute = 0
        self.second = 0


def time(hour, minute, second):
    hour = int(input("Enter hour: "))
    minute = int(input("Enter Minute: "))
    second = int(input("Enter Second: "))
    time_properties.hour = hour
    time_properties.minute = minute
    time_properties.second = second


def validate_hour(hour):
    if hour > 0 & hour <= 12:
        time_properties.hour = hour


def average(nums):
    total = sum(nums)
    size = len(nums)
    avg = total/size
    return avg
