#5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.

from functools import reduce

numbers = [item for item in range(100, 1000 + 1) if item % 2 == 0]
multiplicarion = reduce(lambda x, y: x * y, numbers, 1)
print(multiplicarion)
