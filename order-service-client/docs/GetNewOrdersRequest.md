# GetNewOrdersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **int** | Channel ID through which the request is made | 
**device_id** | **str** | Unique device identifier | [optional] 
**device_type** | **str** | Type of the device | [optional] 
**user_id** | **int** | User ID making the request | [optional] 
**token** | **str** | Session Token | [optional] 

## Example

```python
from order_api_client.models.get_new_orders_request import GetNewOrdersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetNewOrdersRequest from a JSON string
get_new_orders_request_instance = GetNewOrdersRequest.from_json(json)
# print the JSON string representation of the object
print(GetNewOrdersRequest.to_json())

# convert the object into a dict
get_new_orders_request_dict = get_new_orders_request_instance.to_dict()
# create an instance of GetNewOrdersRequest from a dict
get_new_orders_request_from_dict = GetNewOrdersRequest.from_dict(get_new_orders_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


