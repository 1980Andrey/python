#Задание No 2

class Road:
    __asphalt_mass = 25

    def __init__(self, length, width):
        """
        :param length: digit: road length in meters
        :param width: digit: road width in meters
        """
        self._length = float(length)
        self._width = float(width)

    def asphalt_sum(self, thickness=1):
        return self._length * self._width * self.__asphalt_mass * thickness
