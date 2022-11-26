from players.src.enums.player_enums import Statuses
from players.src.builders.localize import localize
from players.src.baseclasses.nest_builder import NestBuilder


class PlayerBuilder(NestBuilder):
    """Класс-билдер, который генерирует необходимый объект. Использованы классические сеттеры."""
    def __init__(self):
        super().__init__()
        self.result = {}  # Пустой словарь, который можно декодировать в json
        self.reset()  # Сразу же наполняем объект значениями по умолчанию

    def set_status(self, status=Statuses.ACTIVE.value):
        """Билдим статус игрока - по умолчанию активен."""
        self.result["account_status"] = status
        return self  # Возвращаем обновленный экземпляр, его же будем достраивать

    def set_balance(self, balance=10):
        """Билдим баланс игрока - по умолчанию равен нулю."""
        self.result["balance"] = balance
        return self

    def set_localize(self, localize=localize):
        """Билдим вложенность - локализацию."""
        self.result["localize"] = localize
        return self

    def set_avatar(self, avatar="https://google.com"):
        """Билдим аватар игрока - по умолчанию равен ссылке на гугл."""
        self.result["avatar"] = avatar
        return self

    def reset(self):
        """Задаем поля по умолчанию."""
        self.set_status()
        self.set_balance()
        self.set_localize()
        self.set_avatar()
        return self


if __name__ == '__main__':
    # Билдим player'ов
    player = PlayerBuilder().build()
    # player1 = PlayerBuilder().set_balance(20).build()  # Меняем баланс
    # player2 = PlayerBuilder().set_status(Statuses.INACTIVE.value).build()  # Меняем статус
    # player3 = PlayerBuilder().set_status("avfsgvdsbdf").build()  # Меняем статус на невалидный
    print(f"{player=}")
    # print(f"{player1=}")
    # print(f"{player2=}")
    # print(f"{player3=}")

    # Смотрим поля у сгенерированных игроков
    player_keys = [key for key in PlayerBuilder().build()]
    print(player_keys)  # ['account_status', 'balance', 'localize', 'avatar']
