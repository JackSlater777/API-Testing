import os
from definitions import ROOT_DIR


# Константы
LOGIN = 'MGF_EAPI'
APPL_CODE = 'MGF_EAPI_APPL'

# Директория тел для запросов
BODIES_PATH = os.path.join(ROOT_DIR, 'microservices/tests/bodies')

# Для тестов на локальном сервере
LOCAL_WIREMOCK_PORT = 8080
LOCAL_WIREMOCK_URL = f'http://localhost:{LOCAL_WIREMOCK_PORT}'

# Для тестов на клоне
WIREMOCK_PORT = 8081
WIREMOCK_URL = f'http://srv3-amain-a.net.billing.ru:{WIREMOCK_PORT}'

# Версии микросервиса
URL = '/api/partner/uni-pmp/v1/call'
URL_V2 = '/api/partner/uni-pmp/v2/call'
