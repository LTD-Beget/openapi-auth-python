# coding: utf-8

"""
    API Аутентификации

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.1.2
    Generated by: https://openapi-generator.tech
"""

from beget_openapi_auth.paths.v1_auth.post import AuthServiceAuth
from beget_openapi_auth.paths.v1_auth_logout.post import AuthServiceLogout
from beget_openapi_auth.paths.v1_auth_refresh.post import AuthServiceRefreshToken
from beget_openapi_auth.paths.v1_auth_switch.post import AuthServiceSwitchUser


class AuthServiceApi(
    AuthServiceAuth,
    AuthServiceLogout,
    AuthServiceRefreshToken,
    AuthServiceSwitchUser,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
