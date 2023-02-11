#Задание No 2

class CustomZeroDivisioneError(Exception):
    pass


def get_numerator() -> int:
    return int(input("Введите числитель"))


def get_denominator() -> int:
    value = int(input("Введите значинатель"))

    if value == 0:
        raise CustomZeroDivisioneError

    return value


while True:
    try:
        numerator = get_numerator()
        denominator = get_denominator()

        print(f"Результат" = {numerator / denominator})
        except CustomZeroDivisioneError:
        print("Не корректное значение, Вы ввели 0 в качестве знаминателя")
    except CustomZeroDivisioneError:
        break
