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
