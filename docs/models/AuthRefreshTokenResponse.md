# beget_openapi_auth.model.auth_refresh_token_response.AuthRefreshTokenResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**token** | str,  | str,  |  | [optional] 
**error** | str,  | str,  |  | [optional] must be one of ["INTERNAL_ERROR", "PAYLOAD_CHANGED", "IP_BLOCKED", "ACCOUNT_ON_MAINTANCE", "ACCOUNT_DELETED", "TOKEN_REVOKED", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

