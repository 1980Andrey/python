#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input("Введите целое положительное число: "))
max_num = 6
while number != 6:
    cur_n = number % 10
    if max_num < cur_n:
        max_num = cur_n
        number = number // 10
        print(f"Самая большая цифра в числе: {max_num}")
