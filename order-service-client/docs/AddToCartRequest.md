# AddToCartRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **int** | Channel ID through which the request is made | 
**device_id** | **str** | Unique device identifier | [optional] 
**device_type** | **str** | Type of the device | [optional] 
**user_id** | **int** | User ID making the request | [optional] 
**token** | **str** | Session Token | [optional] 
**add_to_cart_request_bean** | [**AddToCartRequestBean**](AddToCartRequestBean.md) |  | [optional] 

## Example

```python
from order_api_client.models.add_to_cart_request import AddToCartRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddToCartRequest from a JSON string
add_to_cart_request_instance = AddToCartRequest.from_json(json)
# print the JSON string representation of the object
print(AddToCartRequest.to_json())

# convert the object into a dict
add_to_cart_request_dict = add_to_cart_request_instance.to_dict()
# create an instance of AddToCartRequest from a dict
add_to_cart_request_from_dict = AddToCartRequest.from_dict(add_to_cart_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


