from math import sqrt


message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
          'квадратного корня из заданного числа'

"""Вычисляет квадратный корень."""


def CalculateSquareRoot(Number):
    return sqrt(Number)


def calc(your_number):
    if your_number <= 0:
        return
    print(f"Мы вычислили корень квадратный из введенного вами числа.  Это будетss:\
     {CalculateSquareRoot(your_number)}")


print(message)
calc(25.5)
