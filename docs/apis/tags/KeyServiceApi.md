<a name="__pageTop"></a>
# beget_openapi_auth.apis.tags.key_service_api.KeyServiceApi

All URIs are relative to *https://api.beget.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**key_service_get_key**](#key_service_get_key) | **get** /v1/auth/key | 

# **key_service_get_key**
<a name="key_service_get_key"></a>
> KeyGetKeyResponse key_service_get_key()



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_auth
from beget_openapi_auth.apis.tags import key_service_api
from beget_openapi_auth.model.key_get_key_response import KeyGetKeyResponse
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
    api_instance = key_service_api.KeyServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.key_service_get_key()
        pprint(api_response)
    except beget_openapi_auth.ApiException as e:
        print("Exception when calling KeyServiceApi->key_service_get_key: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#key_service_get_key.ApiResponseFor200) | OK

#### key_service_get_key.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**KeyGetKeyResponse**](../../models/KeyGetKeyResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

