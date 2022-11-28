# Запуск через терминал:
# pytest -s -v tests/something/test_something.py
# -s - захват и вывод print’ов, размещенных внутри тестов в результаты тестов (без -s print’ы в терминал не выводятся).
# -v - более наглядный принт результата теста: имя теста - result.
# -k <имя+маркера> - запуск тестов, маркированных определенным декоратором.
# --duration=<сек> - отметка тестов, проходящих дольше указанного времени, как slowest.
# -vv - флаг к предыдущему аргументу, выводит статистику по slowest тестам: время на setup, тест и teardown.

# Установить allure-pytest:
# pip install allure-pytest
# Для генерации файлов отчета allure:
# pytest -v tests/something/test_something.py --alluredir=results
# Не забыть добавить папку results в .gitignore.
# Для отображения отчета в локальном сервере в браузере в командной строке в папке с проектом:
# allure serve results

# Собираем контейнер. Для этого в терминале выполняем:
# docker build –t automation-tests .
# Если докер-файл лежит не в корне, вместо точки пишем -f <путь/файл>
# docker build -t automation-tests -f users/Dockerfile .
# Для запуска контейнера выполняем:
# docker run automation-tests

# Эти 2 команды нужны, чтобы скопировать данные из контейнера и сгенерировать из результата репорт:
# docker cp $(docker ps -a -q | head -1):/usr/lessons/allureResults .
# allure serve allureResults/
# Две команды ниже, помогут вам, чтобы почистить компьютер:
# docker rm $(docker ps -a -q)
# docker kill $(docker ps -q)
