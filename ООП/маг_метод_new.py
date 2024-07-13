# Реализация магического метода __new__

class Point:
    def __new__(cls, *args, **kwargs):
        print('Вызов метода __new__ для' + str(cls))  # Убедимся что маг метод вызывается
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        print('Вызов метода __init__ для' + str(self))
        self.x = x
        self.y = y


# pt = Point(1,2)
# print(pt, pt.x, pt.y)


# Частичная реализация паттерна Singleton

class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'Соединение с БД: {self.user}, {self.psw}, {self.port}')

    def close(self):
        print('Закрытие соединения с БД')

    def read(self):
        return 'Данные из БД'

    def write(self, data):
        print(f'Запись в БД {data}')


db = DataBase('root', 1234, 40)
db2 = DataBase('root2', 12345, 45)
print(id(db), id(db2))