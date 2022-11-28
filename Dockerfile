# # # Стадия сборки:
# Указываем с какого имейджа нужно собрать контейнер
# Варианты "гарниров" смотрим на dockerhub
FROM python:3.10-alpine

# Блок для формирования переменных окружения:
# ARG применяется только для фазы сборки. Указываем переменную окружения под флаг теста:
# ARG run_env=development
# ENV применяется для исполнения кода внутри контейнера - run_env парсится и закидывается в контейнер
# ENV env $run_env

# Блок для информации об авторе образа:
LABEL "creator"="Ivan"
LABEL "email"="dualking1991@gmail.com"

# Создаём вольюм, для того, чтобы иметь возможность получить данные после того, как контейнер закончит свою работу
VOLUME /allureResults

# Копируем отдельно наш файл с зависимостями (проверяем хеш-сумму слоя)
# Если requirements изменились, то контейнер пересоберется
COPY ./users/requirements.txt ./users/

# Устанавливаем наши зависимости внутри контейнера
RUN pip3 install -r users/requirements.txt

# Этой командой обновляем наш базовый образ и ставим bash
RUN apk update && apk upgrade && apk add bash

# Копируем содержимое проекта внутрь контейнера
COPY . .

# # # Стадия запуска:
# Для запуска тестов с определенными переменными окружения
# CMD pytest -m "$env" -s -v users/tests/* --alluredir=allureResults
CMD pytest -s -v users/tests/* --alluredir=allureResults
