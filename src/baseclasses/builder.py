# Универсальный генератор со вложенностями

class BuilderBaseClass:
    # Пустой json
    def __init__(self):
        self.result = {}

    # Замена значения выборному ключу (подойдет даже для глубоко вложенных)
    def update_inner_value(self, keys, value):
        # Если значение не массив - обновляем (для обновления верхнего уровня)
        if not isinstance(keys, list):
            self.result[keys] = value
        # Для вложенностей
        else:
            # Переменная для многоуровневых данных
            temp = self.result
            for item in keys[:-1]:  # Последний элемент и нужен нам
                # Если ключ НЕ существует, создаем его с пустым значением
                if item not in temp.keys():
                    temp[item] = {}
                # В любом случае переходим на уровень ниже
                temp = temp[item]
            # Присваиваем значение последнему члену
            temp[keys[-1]] = value
        return self

    # Стоппер - возвращаем сгенерированного пользователя
    # см. parent BuilderBasClass
    def build(self):
        return self.result
