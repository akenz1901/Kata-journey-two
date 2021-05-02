class NotAnEvenNumberException(BaseException):

    def __init__(self, message="Not an even number"):
        super(NotAnEvenNumberException, self).__init__(message)


class EvenNumber:

    def __init__(self, number: int):
        if number % 2 == 1:
            raise NotAnEvenNumberException()
        self.__number: int = number

    def get(self):
        return self.__number

    def __add__(self, other_even_number: 'EvenNumber') -> int:
        ans = self.__number + other_even_number.get()
        return ans

    def __str__(self):
        return 'EvenNumber({})'.format(self.__rep__())

    def __rep__(self):
        return EvenNumber(2)
