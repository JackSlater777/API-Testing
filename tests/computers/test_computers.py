# Тестируем: examples.py
# Схема: src/schemas/computer.py

# Запуск через терминал
# pytest -s -v tests/computers/test_computers.py
# -v - более детальный принт результата теста
# -s - отображение принтов внутри тестов
# --duration=int -vv - все тесты, прохождение которых займет более int секунд, будут отмечены, как slowest

# Для генерации файлов отчета allure
# pytest -s -v tests/computers/test_computers.py --alluredir=results
# Не забыть добавить папку results в .gitignore
# Для отображения отчета в браузере в командной строке в папке с проектом
# allure serve results

# import pytest
# from src.baseclasses.response_2 import Response
from src.schemas.computer import Computer
from examples import computer


# Тесты для компьютера
def test_pydantic_object():
    # Получаем спаршенный объект (прописан в методе baseclasses/response_2/validate)
    comp = Computer.parse_obj(computer)
    # Выводим фото
    print(comp.detailed_info.physical.photo)
    # Выводим хост
    print(comp.detailed_info.physical.photo.host)
