# AddToCartResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**Status**](Status.md) |  | [optional] 
**add_to_cart_response_bean** | [**AddToCartResponseBean**](AddToCartResponseBean.md) |  | [optional] 

## Example

```python
from order_api_client.models.add_to_cart_response import AddToCartResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddToCartResponse from a JSON string
add_to_cart_response_instance = AddToCartResponse.from_json(json)
# print the JSON string representation of the object
print(AddToCartResponse.to_json())

# convert the object into a dict
add_to_cart_response_dict = add_to_cart_response_instance.to_dict()
# create an instance of AddToCartResponse from a dict
add_to_cart_response_from_dict = AddToCartResponse.from_dict(add_to_cart_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


