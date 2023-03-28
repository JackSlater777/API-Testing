from wiremock.client import *


local = Mapping(
    scenarioName='local',
    request=MappingRequest(
        method=HttpMethods.GET,
        url='/hello'
    ),
    response=MappingResponse(
        status=407,
        # bodyFileName='mapping_local.json',  # Путь до файла в папке __files
        # headers={"Content-Type": "application/json"}

        # jsonBody={"body": "Nobody is at home!"},  # Боди в виде json'a
        # headers={"Content-Type": "application/json"}

        body='Nobody is at home!',
        headers={"Content-Type": "text/plain"}
    )
)

proxying_to_google = Mapping(
    request=MappingRequest(
        method=HttpMethods.GET,
        urlPattern='.*'
    ),
    response=MappingResponse(
        proxyBaseUrl="https://www.google.com"  # Проксирование базового урла на google
    )
)

vasp_act = Mapping(
    scenarioName='vasp_act',
    request=MappingRequest(
        method=HttpMethods.GET,
        url='/cpapsm/api/cp/v2/subscription?status=new'
    ),
    response=MappingResponse(
        status=200,
        jsonBody=None,
        headers={"Content-Type": "application/json"}
    )
)

vasp_checkpartner_417 = Mapping(
    scenarioName='vasp_checkpartner_417',
    request=MappingRequest(
        method=HttpMethods.GET,
        url='/cpapsm/api/cp/v1/checkpartner?msisdn=79202599494'
    ),
    response=MappingResponse(
        status=417,
        jsonBody=None,
        headers={"Content-Type": "application/json"}
    )
)


if __name__ == "__main__":
    print(vasp_act.get_json_data())  # Конвертируем мок в python-объект
    print(vasp_act.to_json())  # Конвертируем мок в json
