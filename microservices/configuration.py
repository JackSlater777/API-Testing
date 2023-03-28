import os
from definitions import ROOT_DIR


# Константы
LOGIN = 'MGF_EAPI'
APPL_CODE = 'MGF_EAPI_APPL'

# Директория тел для запросов
BODIES_PATH = os.path.join(ROOT_DIR, 'microservices/tests/bodies')

# Для тестов на локальном сервере
LOCAL_WIREMOCK_PORT = 8080
LOCAL_WIREMOCK_HOST = f'http://localhost:{LOCAL_WIREMOCK_PORT}'

# Для тестов на клоне
# WIREMOCK_PORT = 8200
# WIREMOCK_HOST = f'http://srv2-gf-app02:8200'

# Версии микросервиса
URL = '/api/partner/uni-pmp/v1/call'
URL_V2 = '/api/partner/uni-pmp/v2/call'
