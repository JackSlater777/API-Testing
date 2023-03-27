from wiremock.client import *


local = Mapping(
    request=MappingRequest(
        method=HttpMethods.GET,
        url='/hello'
    ),
    response=MappingResponse(
        status=407,
        # bodyFileName='mapping_local.json'  # Путь до файла в папке __files
        # headers={"Content-Type": "application/json"},

        # jsonBody={"body": "Nobody is at home!"},  # Боди в виде json'a
        # headers={"Content-Type": "application/json"},

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

vasp_checkpartner_417 = Mapping(
    request=MappingRequest(
        method=HttpMethods.GET,
        url='/eapi/cutemock-app/v1/api/cpapsm/api/cp/v1/checkpartner'
    ),
    response=MappingResponse(
        status=417,
        bodyFileName='vasp_checkpartner_417.json',  # Путь до файла в папке __files
        headers={"Content-Type": "application/json"}
    )
)


if __name__ == "__main__":
    print(local.get_json_data())  # Конвертируем мок в python-объект
    print(local.to_json())  # Конвертируем мок в json
