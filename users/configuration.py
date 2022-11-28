import os
from definitions import ROOT_DIR


SERVICE_URL = "https://gorest.co.in/public/v1/users"

JSON_RELATIVE_PATH = 'users/src/jsons/response.json'
FOLDER_PATH = 'users/src/jsons'
JSON_PATH = os.path.join(ROOT_DIR, JSON_RELATIVE_PATH)
