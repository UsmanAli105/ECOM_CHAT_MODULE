# AddToCartResponseBean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**current_cart_size** | **int** |  | [optional] 

## Example

```python
from order_api_client.models.add_to_cart_response_bean import AddToCartResponseBean

# TODO update the JSON string below
json = "{}"
# create an instance of AddToCartResponseBean from a JSON string
add_to_cart_response_bean_instance = AddToCartResponseBean.from_json(json)
# print the JSON string representation of the object
print(AddToCartResponseBean.to_json())

# convert the object into a dict
add_to_cart_response_bean_dict = add_to_cart_response_bean_instance.to_dict()
# create an instance of AddToCartResponseBean from a dict
add_to_cart_response_bean_from_dict = AddToCartResponseBean.from_dict(add_to_cart_response_bean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


