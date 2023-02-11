#Задание №4

class Sklad:
    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year
        self.printer_dict = {}
        self.scaner_dict = {}
        self.xerox_dict = {}

    def __str__(self):
        return f'Добавляем на склад:---> \n Модель:{self.name}\n сделано в:{self.make}\n Год выпуска:{self.year}\n'

    def add_Info)

    :

    class Printer(Sklad):
        def __init__(self, name, make, year):
            super().__init__(name, make, year)
            self.printer_dict = []

    class Scaner(Sklad):
        def __init__(self, name, make, year):
            super().__init__(name, make, year)
            self.scaner_dict = []

    class Xerox(Sklad):
        def __init__(self, name, make, year):
            super().__init__(name, make, year)
            self.xerox_dict = []

    p_1 = add_Printer('hundai', 'Russia', 2023)
    p_2 = add_Scaner('sony', 'China', 2022)
    p_3 = add_Xerox('bosh', 'Taiwan', 2023)
