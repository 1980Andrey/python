#Задание No 4

class Car:
    def __init__(self, color: str, name: str, speed: float = 0, is_police: bool = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Car is go')

    def stop(self):
        print('Car stopped')

    def turn(self, direction):
        if direction in ('left', 'right'):
            print(f'Car turn to {direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('ALARM')
        print(self.speed)


class SportCar(Car):
    pass


class WorkCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, color, name, is_sherif):
        self.is_sherif = is_sherif
        super().__init__(color, name, float('inf'), True)


temp = PoliceCar('red', 'Merthy', False)

print(1)
