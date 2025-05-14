# ViewCartBean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cart_id** | **int** |  | [optional] 
**cart_items** | [**List[CartItemBean]**](CartItemBean.md) |  | [optional] 
**total_bill** | **float** |  | [optional] 
**note** | **str** |  | [optional] 

## Example

```python
from order_api_client.models.view_cart_bean import ViewCartBean

# TODO update the JSON string below
json = "{}"
# create an instance of ViewCartBean from a JSON string
view_cart_bean_instance = ViewCartBean.from_json(json)
# print the JSON string representation of the object
print(ViewCartBean.to_json())

# convert the object into a dict
view_cart_bean_dict = view_cart_bean_instance.to_dict()
# create an instance of ViewCartBean from a dict
view_cart_bean_from_dict = ViewCartBean.from_dict(view_cart_bean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


