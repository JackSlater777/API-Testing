import os
from definitions import ROOT_DIR


# BODIES_RELATIVE_PATH = 'microservices/'
# BODIES_PATH = os.path.join(ROOT_DIR, BODIES_RELATIVE_PATH)
BODIES_PATH = os.path.join(ROOT_DIR, 'microservices/tests/bodies')

WIREMOCK_PORT = 8080
WIREMOCK_HOST = f'http://localhost:{WIREMOCK_PORT}'

# Должен быть раскатан:
# WIREMOCK_PORT = 8200
# WIREMOCK_HOST = f'http://srv2-gf-app02:8200'

URL_V2 = '/api/partner/uni-pmp/v2/call'
