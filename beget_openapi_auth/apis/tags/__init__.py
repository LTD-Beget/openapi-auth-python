# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from beget_openapi_auth.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    AUTH_SERVICE = "AuthService"
    KEY_SERVICE = "KeyService"
