# DeleteFromCartRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **int** | Channel ID through which the request is made | 
**device_id** | **str** | Unique device identifier | [optional] 
**device_type** | **str** | Type of the device | [optional] 
**user_id** | **int** | User ID making the request | [optional] 
**token** | **str** | Session Token | [optional] 
**delete_from_cart_request_bean** | [**DeleteFromCartRequestBean**](DeleteFromCartRequestBean.md) |  | [optional] 

## Example

```python
from order_api_client.models.delete_from_cart_request import DeleteFromCartRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteFromCartRequest from a JSON string
delete_from_cart_request_instance = DeleteFromCartRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteFromCartRequest.to_json())

# convert the object into a dict
delete_from_cart_request_dict = delete_from_cart_request_instance.to_dict()
# create an instance of DeleteFromCartRequest from a dict
delete_from_cart_request_from_dict = DeleteFromCartRequest.from_dict(delete_from_cart_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


