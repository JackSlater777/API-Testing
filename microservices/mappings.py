from wiremock.client import *


mapping = Mapping(
   request=MappingRequest(
       method=HttpMethods.GET,
       url='/hello'
   ),
   response=MappingResponse(
       status=200,
       body='hi'
   )
)


if __name__ == "__main__":
    print(mapping.get_json_data())  # Convert mappings to a python object
    print(mapping.to_json())  # Convert mappings to json
