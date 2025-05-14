# UpdateOrderStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **int** | Channel ID through which the request is made | 
**device_id** | **str** | Unique device identifier | [optional] 
**device_type** | **str** | Type of the device | [optional] 
**user_id** | **int** | User ID making the request | [optional] 
**token** | **str** | Session Token | [optional] 
**update_order_request** | [**UpdateOrderStatusRequestBean**](UpdateOrderStatusRequestBean.md) |  | [optional] 

## Example

```python
from order_api_client.models.update_order_status_request import UpdateOrderStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrderStatusRequest from a JSON string
update_order_status_request_instance = UpdateOrderStatusRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateOrderStatusRequest.to_json())

# convert the object into a dict
update_order_status_request_dict = update_order_status_request_instance.to_dict()
# create an instance of UpdateOrderStatusRequest from a dict
update_order_status_request_from_dict = UpdateOrderStatusRequest.from_dict(update_order_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


