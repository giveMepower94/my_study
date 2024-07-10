try:
    with open('write_file.txt', 'w', encoding='utf-8') as file:
        if file.write('Привет! Тестовая запись в файл!'):
            print('Файл записан')
        else:
            print('Ошибка записи в файл')
except:
    print('Ошибка при открытии файла')