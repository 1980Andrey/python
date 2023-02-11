#ЗаданиеNo3

class NonNumberListValueException(Exception):
    pass


numbers = []


def append_numbers(numbers_list: list):
    value = input("Введите число")

    try:
        numbers_list.append(float(value))
    except ValueError:
        raise NonNumberListValueException(f"Вы ввели '{value}' вместо числа")


while True:
    try:
        append_numbers(numbers)
    except NonNumberListValueException as exception:
        print(exception)
    except KeyboardInterrupt:
        print(f"\nСписок числа = {numbers}")
        break
