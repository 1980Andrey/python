# Задание 1

string = []

while True:
    with open('task1.txt', 'a+') as f:
        string = input("Введите строку:")

        if not string:
            break

        f.write(f"{string}\n")
