# Success

try:
    file = open('sample2.txt', encoding='utf-8')
    try:
        read_file = file.read()
        print(read_file)
    finally:
        file.close()
except FileNotFoundError:
    print("Файл не найден")
except:
    print("Произошла ошибка во время чтения файла")

# Error

try:
    file = open('sample3.txt', encoding='utf-8')
    try:
        read_file = file.read()
        int(read_file)
        print(read_file)
    finally:
        file.close()
except FileNotFoundError:
    print("Файл не найден")
except:
    print("Произошла ошибка во время чтения файла")



# Context manager with

try:
    with open('sample2.txt', encoding='utf-8') as file:
        read_file = file.read()
        print(read_file)
except FileNotFoundError:
    print("Файл не найден")
except:
    print("Произошла ошибка во время чтения файла")


# Error

try:
    with open('sample2.txt', encoding='utf-8') as file:
        read_file = file.read()
        int(read_file)
        print(read_file)
except FileNotFoundError:
    print("Файл не найден")
except:
    print("Произошла ошибка во время чтения файла")