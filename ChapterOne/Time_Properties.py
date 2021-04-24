class Time_properties(object):

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __validate_hour(self, hour):
        if 0 < hour > 12:
            raise ValueError("Invalid Input")
        self.hour = hour

    def __validate_minute(self, minute):
        if 60 < minute > 0:
            raise ValueError("Invalid Minute Input")
        self.minute = minute

    def __validate_second(self, second):
        if 0 < second > 60:
            raise ValueError("Invalid Minute Input")
        self.second = second

    def time(self, hour, minute, second):
        self.__validate_hour(hour)
        self.__validate_minute(minute)
        self.__validate_second(second)

    def __str__(self):
        return f'{self.hour}:{self.minute}:{self.second}'


time = Time_properties()
time.time(0, 60, 0)
print(time.__str__())

# # def average(nums):
# #     total = sum(nums)
# #     size = len(nums)
# #     avg = total / size
# #     return avg
