#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

month = int(input("Укажите номер месяца по порядку:"))

seasons_dict = {'зима': (12, 1, 2),
                'весна': (3, 4, 5),
                'лето': (6, 7, 8),
                'осень': (9, 10, 11), }

for seasons, months in seasons_dict.items():
    if month in months:
        print(f"Сейчас да будет: {seasons}")
