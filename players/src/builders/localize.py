from faker import Faker
from random import randint
from players.src.baseclasses.nest_builder import NestBuilder


class LocalizeBuilder(NestBuilder):
    """Класс-билдер, который генерирует вложенность. Использованы классические сеттеры."""
    def __init__(self, lang):
        super().__init__()
        self.lang = lang
        self.result = {}
        self.reset()  # Сразу же наполняем объект значениями по умолчанию

    def set_nickname(self):
        """Билдим никнейм игрока - по умолчанию ."""
        self.result["nickname"] = Faker(self.lang).name()
        return self

    def set_country(self):
        """Билдим неровную вложенность - страну и случайное значение."""
        if self.lang == "en_US":
            self.result["countries"] = {"UA": randint(0, 10)}
        return self

    def reset(self):
        """Задаем поля по умолчанию."""
        self.set_nickname()
        self.set_country()
        return self


# Билдим localize
localize = {
    "en": LocalizeBuilder("en_US").build(),
    "ru": LocalizeBuilder("ru_RU").build()
}


if __name__ == '__main__':
    print(f"{localize=}")
