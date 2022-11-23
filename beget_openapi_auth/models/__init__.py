# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from beget_openapi_auth.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from beget_openapi_auth.model.auth_auth_request import AuthAuthRequest
from beget_openapi_auth.model.auth_auth_response import AuthAuthResponse
from beget_openapi_auth.model.auth_refresh_token_response import AuthRefreshTokenResponse
from beget_openapi_auth.model.auth_switch_user_request import AuthSwitchUserRequest
from beget_openapi_auth.model.auth_switch_user_response import AuthSwitchUserResponse
from beget_openapi_auth.model.key_get_key_response import KeyGetKeyResponse
