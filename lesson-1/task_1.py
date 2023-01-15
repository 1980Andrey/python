# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.

user_name = 'Андрей'
user_surname = 'Павлов'
age = 42

print('Привет!', user_name, user_surname, age, 'лет')

user_name = input("Введите Ваше имя: ")
user_surname = input("Введите Вашу фамилию: ")
age = input("Введите Ваш возраст: ")
print(f"Ваши данные для входа в аккаунт: имя - {user_name}, фамилия - {user_surname},"
      f"возраст - {age}")

number_1 = int(input("Введите любое число: "))
number_2 = int(input("Введите другое любое число: "))
number_3 = int(input("Введите еще одно другое любое число: "))
sum = number_1 + number_2 + number_3
print("Сумма чисел равна: ", sum)

text = input("Введите текст")
another_text = input("Введите другой текст")
print(text)
print(another_text)