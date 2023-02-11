#Задание No 3

class Cell:
    def __init__(self, cell_count):
        self.__cell_count = cell_count

    @property
    def cell_count(self):
        return self.__cell_count

    def __add__(self, other):
        """Сложение. Объединение двух клеток.
        При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток."""

        return Cell(self.cell_count + other.cell_count)

    def __sub__(self, other):
        """ todo Вычитание. Участвуют две клетки.
#Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.
"""
        pass

    def __truediv__(self, other):
        # Деление
        pass

    def __mul__(self, other):
        # Умножение
        pass

    def __floordiv__(self, other):
        # целочисленное деление
        pass

    def make_order(self, lines: int):
        temp = self.cell_count // lines
        result = '/n'.join(['*' for _ in range(temp)])
