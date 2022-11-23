# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from beget_openapi_auth.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_AUTH = "/v1/auth"
    V1_AUTH_KEY = "/v1/auth/key"
    V1_AUTH_LOGOUT = "/v1/auth/logout"
    V1_AUTH_REFRESH = "/v1/auth/refresh"
    V1_AUTH_SWITCH = "/v1/auth/switch"
