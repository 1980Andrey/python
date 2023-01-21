#6. Реализовать два небольших скрипта:
#итератор, генерирующий целые числа, начиная с указанного;
#итератор, повторяющий элементы некоторого списка, определённого заранее. Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения. #### Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 — завершаем цикл.
# Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.

from itertools import count, cycle

print("*" * 20, "Iterator A")
start_interator = 7

for el in count(start_interator):
    if el > 10:
        break

    print(el)

print("*" * 20, "Iterator B")
cycling_list = [4, 8, 15, 16, 23, 42]
max_iterations = 12
iterations_count = 0

for el in cycle(cycling_list):
    print(el)
    iterations_count += 1

    if iterations_count >= max_iterations:
        break
