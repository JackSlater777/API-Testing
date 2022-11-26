from databases.src.baseclasses.nest_builder import NestBuilder
from faker import Faker


class ItemTypeBuilder(NestBuilder):
    """Класс-билдер, который генерирует необходимый объект. Использованы классические сеттеры."""
    def __init__(self):
        super().__init__()
        self.result = {}  # Пустой словарь, который можно декодировать в json
        self.reset()  # Сразу же наполняем объект значениями по умолчанию

    def set_item_type(self, item_type=Faker().word()):
        """"""
        self.result['item_type'] = item_type
        return self

    def reset(self):
        """Задаем поля по умолчанию."""
        self.set_item_type()
        return self


if __name__ == '__main__':
    # Билдим item_type:
    item_type = ItemTypeBuilder().build()
    print(f"{item_type=}")  # item_type={'item_type': 'fine'}

    # Смотрим поля у сгенерированных игроков
    item_type_keys = [key for key in ItemTypeBuilder().build()]
    print(item_type_keys)  # ['item_type']
