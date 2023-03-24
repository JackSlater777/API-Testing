from wiremock.server import WireMockServer
from wiremock.constants import Config
from wiremock.client import *
from microservices_with_wiremock.mappings import mapping
import requests
import time


wm = WireMockServer()
wm.port = 8080  # By default
server_url = f'http://localhost:{wm.port}'
Config.base_url = f'http://localhost:{wm.port}/__admin'
wm.start()  # Server is up
Mappings.delete_all_mappings()  # Clean up
mapping = Mappings.create_mapping(mapping=mapping)  # Set up stubs
requests.post(f'{Config.base_url}/mappings/save')  # Save mappings into json file in the mappings folder
response = requests.get(f'{server_url}/hello')  # Make API calls
print(response)  # <Response [200]>
print(response.text)  # hi
time.sleep(5)
wm.stop()  # Server is down
