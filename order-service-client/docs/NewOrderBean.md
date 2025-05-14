# NewOrderBean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_details** | [**OrderBean**](OrderBean.md) |  | [optional] 
**order_items** | [**List[OrderItemBean]**](OrderItemBean.md) |  | [optional] 

## Example

```python
from order_api_client.models.new_order_bean import NewOrderBean

# TODO update the JSON string below
json = "{}"
# create an instance of NewOrderBean from a JSON string
new_order_bean_instance = NewOrderBean.from_json(json)
# print the JSON string representation of the object
print(NewOrderBean.to_json())

# convert the object into a dict
new_order_bean_dict = new_order_bean_instance.to_dict()
# create an instance of NewOrderBean from a dict
new_order_bean_from_dict = NewOrderBean.from_dict(new_order_bean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


