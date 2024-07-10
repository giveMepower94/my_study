file = open('sample2.txt', encoding='utf-8')  # чтение файла sample2.txt в кодировке utf-8

# print(file.read())  # чтение всего файла

# print(file.readline())  # чтение первой строки

for line in file:
    print(line, end='') # чтение всего файла по строкам

file.close()  # закрытие файла, не обязательно, но лучше всегда закрывать файлы