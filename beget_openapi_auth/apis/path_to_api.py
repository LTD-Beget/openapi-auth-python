import typing_extensions

from beget_openapi_auth.paths import PathValues
from beget_openapi_auth.apis.paths.v1_auth import V1Auth
from beget_openapi_auth.apis.paths.v1_auth_key import V1AuthKey
from beget_openapi_auth.apis.paths.v1_auth_logout import V1AuthLogout
from beget_openapi_auth.apis.paths.v1_auth_refresh import V1AuthRefresh
from beget_openapi_auth.apis.paths.v1_auth_switch import V1AuthSwitch

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_AUTH: V1Auth,
        PathValues.V1_AUTH_KEY: V1AuthKey,
        PathValues.V1_AUTH_LOGOUT: V1AuthLogout,
        PathValues.V1_AUTH_REFRESH: V1AuthRefresh,
        PathValues.V1_AUTH_SWITCH: V1AuthSwitch,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_AUTH: V1Auth,
        PathValues.V1_AUTH_KEY: V1AuthKey,
        PathValues.V1_AUTH_LOGOUT: V1AuthLogout,
        PathValues.V1_AUTH_REFRESH: V1AuthRefresh,
        PathValues.V1_AUTH_SWITCH: V1AuthSwitch,
    }
)
