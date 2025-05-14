# AddToCartRequestBean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**unit_price** | **float** |  | [optional] 

## Example

```python
from order_api_client.models.add_to_cart_request_bean import AddToCartRequestBean

# TODO update the JSON string below
json = "{}"
# create an instance of AddToCartRequestBean from a JSON string
add_to_cart_request_bean_instance = AddToCartRequestBean.from_json(json)
# print the JSON string representation of the object
print(AddToCartRequestBean.to_json())

# convert the object into a dict
add_to_cart_request_bean_dict = add_to_cart_request_bean_instance.to_dict()
# create an instance of AddToCartRequestBean from a dict
add_to_cart_request_bean_from_dict = AddToCartRequestBean.from_dict(add_to_cart_request_bean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


