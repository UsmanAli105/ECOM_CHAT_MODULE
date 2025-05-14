# DeleteFromCartResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**Status**](Status.md) |  | [optional] 
**delete_from_cart_response_bean** | [**DeleteFromCartResponseBean**](DeleteFromCartResponseBean.md) |  | [optional] 

## Example

```python
from order_api_client.models.delete_from_cart_response import DeleteFromCartResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteFromCartResponse from a JSON string
delete_from_cart_response_instance = DeleteFromCartResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteFromCartResponse.to_json())

# convert the object into a dict
delete_from_cart_response_dict = delete_from_cart_response_instance.to_dict()
# create an instance of DeleteFromCartResponse from a dict
delete_from_cart_response_from_dict = DeleteFromCartResponse.from_dict(delete_from_cart_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


