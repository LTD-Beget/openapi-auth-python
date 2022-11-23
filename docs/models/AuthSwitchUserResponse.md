# beget_openapi_auth.model.auth_switch_user_response.AuthSwitchUserResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**token** | str,  | str,  |  | [optional] 
**error** | str,  | str,  |  | [optional] must be one of ["INTERNAL_ERROR", "EMPTY_TARGET_LOGIN", "TARGET_FORBIDDEN", "TARGET_NOT_FOUND", "TARGET_PASSWORD_REQUIRED", "TARGET_CODE_REQUIRED", "TARGET_INCORRECT_CODE", "SENT_LIMIT_REACHED", "INPUT_LIMIT_REACHED", "TARGET_ON_MAINTENANCE", "TARGET_DELETED", "TOKEN_REVOKED", "CODE_REQUIRED_EMAIL", "CODE_REQUIRED_SMS", "IP_BLOCKED", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

