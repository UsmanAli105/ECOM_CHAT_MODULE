# OrderItemBean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**price** | **float** |  | [optional] 

## Example

```python
from order_api_client.models.order_item_bean import OrderItemBean

# TODO update the JSON string below
json = "{}"
# create an instance of OrderItemBean from a JSON string
order_item_bean_instance = OrderItemBean.from_json(json)
# print the JSON string representation of the object
print(OrderItemBean.to_json())

# convert the object into a dict
order_item_bean_dict = order_item_bean_instance.to_dict()
# create an instance of OrderItemBean from a dict
order_item_bean_from_dict = OrderItemBean.from_dict(order_item_bean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


