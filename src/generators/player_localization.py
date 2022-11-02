from faker import Faker  # Модуль для генерации имен, адресов, картинок и т.д.


class PlayerLocalization:
    def __init__(self, lang):
        """
        Генерируем вложенный атрибут объекта
        Пример описания билдера для локализации.
        В зависимости от того, какой язык будет передан в этот билдер, на таком
        языке и будет работать наш фейкер. Дальше, дело за малым, объект будет
        наполнен точно так же, как и другие подобные объекты, только каждый на
        своём языке.
        """
        self.fake = Faker(lang)
        self.result = {
            "nickname": self.fake.first_name()
        }

    def set_number(self, number=11):
        """
        Добавляет в результат ключ number, для которого будет использовано
        переданное значение, если же такое отсутствует, то используем значение
        11 по-умолчанию.
        """
        self.result['number'] = number
        return self

    def build(self):
        """
        Возвращает наш обьект в виде JSON.
        """
        return self.result


if __name__ == '__main__':
    rus = PlayerLocalization('ru').build()
    print(rus)
    eng = PlayerLocalization('en').build()
    print(eng)
