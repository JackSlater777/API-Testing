from src.enums.user_enums import Statuses
from src.generators.player_localization import PlayerLocalization
from src.baseclasses.builder import BuilderBaseClass


# Генерируем пользователя (игрока) через билдер (класс с определенными значениями)
# для тестов

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
        super().__init__()
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
                'en': PlayerLocalization('en_US').build(),
                'ru': PlayerLocalization('ru_RU').build()
        }
        return self


if __name__ == '__main__':
    p = Player().build()
    print(p)
