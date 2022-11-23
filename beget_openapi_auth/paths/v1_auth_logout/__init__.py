# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from beget_openapi_auth.paths.v1_auth_logout import Api

from beget_openapi_auth.paths import PathValues

path = PathValues.V1_AUTH_LOGOUT