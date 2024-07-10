import csv

name_1 = 'John'
name_2 = 'Mary'


with open('test.csv', 'w', newline='', encoding='cp1251') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([name_1, name_2])

# Дозаписываем данные в файл

data_file = [
    ['User_1', 'address_1'],
    ['User_2', 'address_2'],
    ['User_3', 'address_3'],
]

for row in data_file:
    with open('test.csv', 'a', newline='', encoding='cp1251') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(row)