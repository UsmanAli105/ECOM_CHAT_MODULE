# SubmitCartRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **int** | Channel ID through which the request is made | 
**device_id** | **str** | Unique device identifier | [optional] 
**device_type** | **str** | Type of the device | [optional] 
**user_id** | **int** | User ID making the request | [optional] 
**token** | **str** | Session Token | [optional] 
**submit_cart_request_bean** | [**SubmitCartRequestBean**](SubmitCartRequestBean.md) |  | [optional] 

## Example

```python
from order_api_client.models.submit_cart_request import SubmitCartRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitCartRequest from a JSON string
submit_cart_request_instance = SubmitCartRequest.from_json(json)
# print the JSON string representation of the object
print(SubmitCartRequest.to_json())

# convert the object into a dict
submit_cart_request_dict = submit_cart_request_instance.to_dict()
# create an instance of SubmitCartRequest from a dict
submit_cart_request_from_dict = SubmitCartRequest.from_dict(submit_cart_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


