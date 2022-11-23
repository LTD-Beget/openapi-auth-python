import typing_extensions

from beget_openapi_auth.apis.tags import TagValues
from beget_openapi_auth.apis.tags.auth_service_api import AuthServiceApi
from beget_openapi_auth.apis.tags.key_service_api import KeyServiceApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.AUTH_SERVICE: AuthServiceApi,
        TagValues.KEY_SERVICE: KeyServiceApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.AUTH_SERVICE: AuthServiceApi,
        TagValues.KEY_SERVICE: KeyServiceApi,
    }
)
