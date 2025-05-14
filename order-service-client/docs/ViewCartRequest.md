# ViewCartRequest


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
from order_api_client.models.view_cart_request import ViewCartRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ViewCartRequest from a JSON string
view_cart_request_instance = ViewCartRequest.from_json(json)
# print the JSON string representation of the object
print(ViewCartRequest.to_json())

# convert the object into a dict
view_cart_request_dict = view_cart_request_instance.to_dict()
# create an instance of ViewCartRequest from a dict
view_cart_request_from_dict = ViewCartRequest.from_dict(view_cart_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


