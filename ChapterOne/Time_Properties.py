class Time_properties:

    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.second = 0

    def __validate_hour(self):
        if self.hour > 0 & self.hour <= 12:
            raise ValueError("Invalid Input")

    def __validate_minute(self):
        if self.minute >= 0 & self.minute <= 60:
            raise ValueError("Invalid Minute Input")

    def __validate_second(self):
        if self.second >= 0 & self.second <= 60:
            raise ValueError("Invalid Minute Input")

    def time(self, hour, minute, second):
        self.__validate_hour()
        self.hour = hour
        self.__validate_minute()
        self.minute = minute
        self.__validate_second()
        self.second = second

    def __str__(self):
        return "{}".format(self.time(40, 50, 70))

    # def average(nums):
    #     total = sum(nums)
    #     size = len(nums)
    #     avg = total / size
    #     return avg
