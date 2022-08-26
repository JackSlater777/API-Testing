# Тестируем:
# https//:my-json-server.typicode.com/typicode/demo/posts

# Запуск через терминал
# pytest -s -v tests/users/test_users.py
# -v - более детальный принт результата теста
# -s - отображение принтов внутри тестов
# --duration=int -vv - все тесты, прохождение которых займет более int секунд, будут отмечены, как slowest

# Для генерации файлов отчета allure
# pytest -s -v tests/users/test_users.py --alluredir=results
# Не забыть добавить папку results в .gitignore
# Для отображения отчета в браузере в командной строке в папке с проектом
# allure serve results

import requests
from configuration import SERVICE_URL

from src.baseclasses.response import Response
# from src.schemas.post import POST_SCHEMA  # json-schema
from src.pydantic_schemas.post import Post  # pydantic-schema


def test_getting_posts():
    """
    Здесь указываем описание теста (появится в allure-description)
    """
    # Получаем данных
    r = requests.get(url=SERVICE_URL)
    # Скармливаем данные в класс
    response = Response(r)
    # Если статус 200, валидируем на соответствие схеме
    # response.assert_status_code(200).validate(POST_SCHEMA)
    response.assert_status_code(200).validate(Post)
