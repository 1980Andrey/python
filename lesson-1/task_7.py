#7. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.


a = int(input("Введите расстояние первой пробежки в км: "))
b = int(input("Введите целевой результат в км: "))

counter = 1

while a < b:
    a *= 1.1
    counter += 1

print(f"На {counter}-й день спортсмен достиг результата — не менее {b} км")
