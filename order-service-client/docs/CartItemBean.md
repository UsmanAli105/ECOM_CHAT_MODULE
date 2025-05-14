# CartItemBean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**price** | **float** |  | [optional] 

## Example

```python
from order_api_client.models.cart_item_bean import CartItemBean

# TODO update the JSON string below
json = "{}"
# create an instance of CartItemBean from a JSON string
cart_item_bean_instance = CartItemBean.from_json(json)
# print the JSON string representation of the object
print(CartItemBean.to_json())

# convert the object into a dict
cart_item_bean_dict = cart_item_bean_instance.to_dict()
# create an instance of CartItemBean from a dict
cart_item_bean_from_dict = CartItemBean.from_dict(cart_item_bean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


