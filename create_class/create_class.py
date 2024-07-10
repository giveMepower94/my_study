# Создаем класс ресторан

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def __str__(self):
        return f'Ресторан: {self.restaurant_name}'

    def describe_restaurant(self):
        return f'Ресторан {self.restaurant_name} c {self.cuisine_type} кухней!'

    def open_restaurant(self):
        return f'Наш ресторан {self.restaurant_name} открыт!'

# Создаем три экземпляра класса и выводим метод describe_restaurant

restik_1 = Restaurant('Бык', 'Русской')

restik_2 = Restaurant('Гилт', 'Итальянской')

restik_3 = Restaurant('Хука', 'Австрийской')

describe_restik_1 =restik_1.describe_restaurant()

describe_restik_2 =restik_2.describe_restaurant()

describe_restik_3 =restik_3.describe_restaurant()

class_example = Restaurant('Nargiliya', 'Русской')


# Создаем класс User

class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f'Меня зовут {self.first_name} - {self.last_name}'

    def describe_user(self):
        return f'Меня зовут {self.first_name} - {self.last_name}, мне {self.age} лет'

    def greet_user(self):
        return f'Привет {self.first_name} - {self.last_name}'


user = User('John', 'Travolta', 45)


# Добавили новый атрибут number_served в класс Restaurant

restik_1 = Restaurant('Бык', 'Русской')

restik_1.number_served = 20

print(f'В нашем ресторане было {restik_1.number_served} посетителей! ')