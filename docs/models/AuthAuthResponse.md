# beget_openapi_auth.model.auth_auth_response.AuthAuthResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**token** | str,  | str,  |  | [optional] 
**error** | str,  | str,  |  | [optional] must be one of ["INTERNAL_ERROR", "EMPTY_LOGIN", "EMPTY_PASSWORD", "INCORRECT_CREDENTIALS", "IP_BLOCKED", "CODE_REQUIRED", "INCORRECT_CODE", "CODE_SENT_LIMIT", "CODE_INPUT_LIMIT", "ACCOUNT_ON_MAINTANCE", "ACCOUNT_DELETED", "CODE_REQUIRED_EMAIL", "CODE_REQUIRED_SMS", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

