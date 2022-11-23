<a name="__pageTop"></a>
# beget_openapi_auth.apis.tags.auth_service_api.AuthServiceApi

All URIs are relative to *https://api.beget.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_service_auth**](#auth_service_auth) | **post** /v1/auth | 
[**auth_service_logout**](#auth_service_logout) | **post** /v1/auth/logout | 
[**auth_service_refresh_token**](#auth_service_refresh_token) | **post** /v1/auth/refresh | 
[**auth_service_switch_user**](#auth_service_switch_user) | **post** /v1/auth/switch | 

# **auth_service_auth**
<a name="auth_service_auth"></a>
> AuthAuthResponse auth_service_auth(auth_auth_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_auth
from beget_openapi_auth.apis.tags import auth_service_api
from beget_openapi_auth.model.auth_auth_response import AuthAuthResponse
from beget_openapi_auth.model.auth_auth_request import AuthAuthRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.beget.com
# See configuration.py for a list of all supported configuration parameters.
configuration = beget_openapi_auth.Configuration(
    host = "https://api.beget.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = beget_openapi_auth.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with beget_openapi_auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_service_api.AuthServiceApi(api_client)

    # example passing only required values which don't have defaults set
    body = AuthAuthRequest(
        login="login_example",
        password="password_example",
        code="code_example",
        save_me=True,
    )
    try:
        api_response = api_instance.auth_service_auth(
            body=body,
        )
        pprint(api_response)
    except beget_openapi_auth.ApiException as e:
        print("Exception when calling AuthServiceApi->auth_service_auth: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthAuthRequest**](../../models/AuthAuthRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#auth_service_auth.ApiResponseFor200) | OK

#### auth_service_auth.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthAuthResponse**](../../models/AuthAuthResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **auth_service_logout**
<a name="auth_service_logout"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} auth_service_logout()



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_auth
from beget_openapi_auth.apis.tags import auth_service_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.beget.com
# See configuration.py for a list of all supported configuration parameters.
configuration = beget_openapi_auth.Configuration(
    host = "https://api.beget.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = beget_openapi_auth.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with beget_openapi_auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_service_api.AuthServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.auth_service_logout()
        pprint(api_response)
    except beget_openapi_auth.ApiException as e:
        print("Exception when calling AuthServiceApi->auth_service_logout: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#auth_service_logout.ApiResponseFor200) | OK

#### auth_service_logout.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **auth_service_refresh_token**
<a name="auth_service_refresh_token"></a>
> AuthRefreshTokenResponse auth_service_refresh_token()



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_auth
from beget_openapi_auth.apis.tags import auth_service_api
from beget_openapi_auth.model.auth_refresh_token_response import AuthRefreshTokenResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.beget.com
# See configuration.py for a list of all supported configuration parameters.
configuration = beget_openapi_auth.Configuration(
    host = "https://api.beget.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = beget_openapi_auth.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with beget_openapi_auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_service_api.AuthServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.auth_service_refresh_token()
        pprint(api_response)
    except beget_openapi_auth.ApiException as e:
        print("Exception when calling AuthServiceApi->auth_service_refresh_token: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#auth_service_refresh_token.ApiResponseFor200) | OK

#### auth_service_refresh_token.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthRefreshTokenResponse**](../../models/AuthRefreshTokenResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **auth_service_switch_user**
<a name="auth_service_switch_user"></a>
> AuthSwitchUserResponse auth_service_switch_user(auth_switch_user_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_auth
from beget_openapi_auth.apis.tags import auth_service_api
from beget_openapi_auth.model.auth_switch_user_request import AuthSwitchUserRequest
from beget_openapi_auth.model.auth_switch_user_response import AuthSwitchUserResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.beget.com
# See configuration.py for a list of all supported configuration parameters.
configuration = beget_openapi_auth.Configuration(
    host = "https://api.beget.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = beget_openapi_auth.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with beget_openapi_auth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_service_api.AuthServiceApi(api_client)

    # example passing only required values which don't have defaults set
    body = AuthSwitchUserRequest(
        login="login_example",
        password="password_example",
        code="code_example",
    )
    try:
        api_response = api_instance.auth_service_switch_user(
            body=body,
        )
        pprint(api_response)
    except beget_openapi_auth.ApiException as e:
        print("Exception when calling AuthServiceApi->auth_service_switch_user: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthSwitchUserRequest**](../../models/AuthSwitchUserRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#auth_service_switch_user.ApiResponseFor200) | OK

#### auth_service_switch_user.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthSwitchUserResponse**](../../models/AuthSwitchUserResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

