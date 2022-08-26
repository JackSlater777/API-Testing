# Генерируем пользователя (игрока) через билдер (класс с определенными значениями) для тестов
from src.enums.user_enums import Statuses
from src.generators.player_localisation import PlayerLocalisation
from src.baseclasses.builder import BuilderBaseClass


# Структура текущего пользователя (json):
# player = {
#     "account_status": "active",
#     "balance": 10,
#     "localize": {
#         "en": {"nickname": "SolveMe", "countries":{"UA": 3}},
#         "ru": {"nickname": "СолвМи"}
#     },
#     "avatar": "https://google.com"
# }


class Player(BuilderBaseClass):
    # Пустой json
    def __init__(self):
        # Наследуемся от общего билдер-класса
        super(Player, self).__init__()
        # Наполнение полей по умолчанию прямо в конструкторе
        self.reset()

    # Задание статуса (активный по умолчанию)
    def set_status(self, status=Statuses.ACTIVE.value):
        # Добавляем в json статус
        self.result['account_status'] = status
        return self

    # Задание баланса (0 по умолчанию)
    def set_balance(self, balance=0):
        self.result['balance'] = balance
        return self

    # Задание аватара
    def set_avatar(self, avatar="https://google.com"):
        self.result['avatar'] = avatar

    # Насыщение полей по умолчанию
    def reset(self):
        self.set_status()
        self.set_balance()
        self.set_avatar()
        self.result["localize"] = {
                # Срандомленные Faker'ом данные
                'en': PlayerLocalisation('en_US').build(),
                'ru': PlayerLocalisation('ru_RU').build()
        }
        return self

    # Замена значения выборному ключу (подойдет даже для глубоко вложенных)
    # см. parent BuilderBasClass

    # Стоппер - возвращаем сгенерированного пользователя
    # см. parent BuilderBasClass


# p = Player().build()
# print(p)
