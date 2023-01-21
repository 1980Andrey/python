#Задание No 4

translation = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре",

}

converted_rows = []

with open("task4.txt") as input_data:
    for row in input_data:
        name, value = row.split(' _ ')
        converted_rows.append(f"{translation[name]} - {value}")

with open("task4_ru.txt", "w") as output_data:
    output_data.writelines(converted_rows)
