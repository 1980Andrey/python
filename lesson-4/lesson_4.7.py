#7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции должен создаваться объект-генератор. Функция вызывается следующим образом: for el in fact(n).
# Она отвечает за получение факториала числа.
# В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.

def fibo_gen():
    prev = 1
    result = 1
    while True:
        yield result
        prev += 1
        result *= prev


for idx, itm in enumerate(fibo_gen(), 1):
    print(idx, itm)
    if idx == 15:
        break
