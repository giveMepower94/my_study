class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        self.x = x
        self.y = y

    def __getattribute__(self, item):
        if item == 'x':
            raise ValueError('Недопустимая переменная')
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'z':
            raise ValueError('Недопустимая переменная')
        return object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        return object.__delattr__(self, item)


p = Point(10, 20)
# print(p.y)
# print(p.pp)