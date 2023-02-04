#Задание No 5

class Stationery:
    title: str
    _message = "Запуск отрисовки"

    def draw(self):
        print(self._message)


class Pen(Stationery):
    _message = "Рисуем ручкой."


class Pencil(Stationery):
    _message = "Рисуем карандашом."


class Handle(Stationery):
    _message = "Рисуем маркером."


items = [Pen(), Pencil(), Handle()]

for item in items:
    item.draw()
