## API-Testing

Тестовый проект поделен на пакеты, в каждом из которых тестируется свой объект: запрос, готовый json или база данных.

users:
- тестовый объект: запрос или json
- реализован mock для requests
- json без вложенностей
- с запросом, mock-запросом и json'ом проводится тест валидации
- для пакета реализован отчет Allure, Dockerfile и pipeline github actions для автоматической сборки образа и его отправки в репозиторий hub.docker.com


players:
- тестовый объект: json
- json с одной НЕРОВНОЙ вложенностью
- с помощью билдеров строится объект архитектуры, идентичный json'у, со случайными данными
- реализован билдер, который генерирует данные на любой глубине вложенности
- с json'ом и построенным объектом проводятся тесты валидации


computers:
- тестовый объект: json
- json с несколькими вложенностями
- показано множество "батареек" pydantic'a в схеме
- с json'ом проводится тест валидации


databases:
- тестовый объект: база данных (файл) SQLite через SQLAlchemy и DB-API
- с помощью билдера строится объект архитектуры, идентичный объекту в таблице базы данных
- с базой данных проводится тест операторов CRUD


microservices:
- тестовый объект: запрос
- продемонстрировано создание response-моков (stub'ов) через скрипт и их сохранение в json-файл
- продемонстрированы запуск сервера через скрипт и отправка запроса по стабу
