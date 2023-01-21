#6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую
# их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func(text):
    return text.title()


def my_title(text):
    listed_text = list(text)
    listed_text[0] = listed_text[0].upper()
    return ''.join(listed_text)


output = []

for word in input('Введите слова через пробелы: ').split(' '):
    output.append(int_func(word))

print(f'Ваши слова выглядят так: {" ".join(output)}')
