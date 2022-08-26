# Генерируем вложенный атрибут объекта

from faker import Faker  # Модуль для генерации имен, адресов, картинок и т.д.


fake = Faker()


class PlayerLocalisation:

    def __init__(self, lang):
        self.fake = Faker(lang)
        self.result = {
            "nickname": self.fake.first_name()
        }

    # Добавление номера пользователя к нику
    def set_number(self, number=11):
        self.result['number'] = number
        return self

    # Стоппер - возвращаем сгенерированное имя
    def build(self):
        return self.result
