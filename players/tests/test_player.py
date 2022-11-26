import pytest
from players.src.enums.player_enums import Statuses
from players.src.schemas.player import Player  # pydantic схема
from players.src.builders.player import PlayerBuilder  # билдер объекта
from players.src.builders.localize import LocalizeBuilder  # билдер вложенности
from players.src.baseclasses.object_validator import ObjectValidator


class TestPlayersAdv:
    def test_json_validation(self, get_data_from_json):
        """Проверяем валидацию json'a."""
        get_data_from_json.validate(Player)  # Валидируем объект
        print(get_data_from_json.get_parsed_item())  # Смотрим результат

    @pytest.mark.parametrize("status", Statuses.list())  # Аналог: [status.value for status in Statuses]
    def test_status_validation(self, status, build_player):
        """Проверяем статус игрока."""
        data = build_player.set_status(status).build()  # Генерируем игроков с перечислениями статусов
        obj = ObjectValidator(data)  # Скармливаем ответ в класс
        obj.validate(Player)  # Валидируем объект
        print(obj.get_parsed_item())  # Смотрим результат

    @pytest.mark.parametrize("balance", [100, 0, -10])
    def test_player_balance_positive(self, balance, build_player):
        """Позитивный тест баланса игрока."""
        data = build_player.set_balance(balance).build()  # Генерируем игроков с разными балансами
        obj = ObjectValidator(data)  # Скармливаем ответ в класс
        obj.validate(Player)  # Валидируем объект
        print(obj.get_parsed_item())  # Смотрим результат

    @pytest.mark.parametrize("balance", ["", "0", "asd", [], tuple(), set(), {}])
    def test_player_balance_negative(self, balance, build_player):
        """Негативный тест баланса игрока."""
        data = build_player.set_balance(balance).build()  # Генерируем игроков с разными балансами
        obj = ObjectValidator(data)  # Скармливаем ответ в класс
        with pytest.raises(AssertionError):
            obj.validate(Player)  # Валидируем объект (ошибка, т.к. негативное тестирование)

    @pytest.mark.parametrize("delete_key", [field for field in PlayerBuilder().build()])
    def test_player_delete_keys(self, delete_key, build_player):
        """Удаляем поля у игрока."""
        default_data = build_player.build()
        del default_data[delete_key]  # Удаляем по очереди каждое поле...
        print(default_data)  # ...и смотрим результат
        obj = ObjectValidator(default_data)  # Скармливаем ответ в класс
        with pytest.raises(AssertionError):
            obj.validate(Player)  # Валидируем объект (ошибка, т.к. не хватает полей)

    @pytest.mark.production
    @pytest.mark.development
    # @pytest.mark.skip('[ISSUE-2341]')
    def test_player_update_localize(self, build_player):
        """Изменяем поле локализации у игрока."""
        # Меняем две локализации на одну французскую.
        changed_data = build_player.update(
            "localize", {"fr": LocalizeBuilder("fr_FR").build()}
        ).build()
        obj = ObjectValidator(changed_data)  # Скармливаем ответ в класс
        with pytest.raises(AssertionError):
            obj.validate(Player)  # Валидируем объект (ошибка, т.к. не хватает полей)

    def test_player_add_localize(self, build_player):
        """Добавляем еще одно поле локализации у игрока."""
        # Добавляем немецкую локализацию.
        changed_data = build_player.update(
            ["localize", "de"], LocalizeBuilder("de_DE").build()
        ).build()
        obj = ObjectValidator(changed_data)  # Скармливаем ответ в класс
        obj.validate(Player)  # Валидируем объект (ошибки нет, т.к. лишние поля, не указанные в схеме, не валидируются)
        print(obj.get_parsed_item())  # Смотрим результат

    @pytest.mark.parametrize(
        "language, localization", [
            ("fr", "fr_FR"), ("de", "de_DE"), ("it", "it_IT")
        ]
    )
    def test_player_add_localizes(self, build_player, language, localization):
        """Добавляем несколько полей с разными локализациями у игрока."""
        # Добавляем  локализацию - и удаляем после валидации - чистим объект
        changed_data = build_player.update(
            ["localize", language], LocalizeBuilder(localization).build()
        ).build()
        obj = ObjectValidator(changed_data)  # Скармливаем ответ в класс
        obj.validate(Player)  # Валидируем объект (ошибки нет, т.к. лишние поля, не указанные в схеме, не валидируются)
        print(obj.get_parsed_item())  # Смотрим результат
        del changed_data["localize"][language]  # Если у объекта нужно удалить добавленную локализацию  (чистка);
        # Т.е. локализации не будут нарастать на объекте.

    def test_player_add_countries(self, build_player):
        """Добавляем ключ страны локализации, у которой его еще нет."""
        # Добавляем поле страны к русской локализации.
        changed_data = build_player.update(
            ["localize", "ru", "countries"], {'RUS': 4}
        ).build()
        obj = ObjectValidator(changed_data)  # Скармливаем ответ в класс
        with pytest.raises(AssertionError):
            obj.validate(Player)  # Валидируем объект (ошибка, т.к. в схеме Country нет поля RUS)


if __name__ == '__main__':
    pytest.main()
