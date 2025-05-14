# OrderBean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **int** |  | [optional] 
**customer_id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from order_api_client.models.order_bean import OrderBean

# TODO update the JSON string below
json = "{}"
# create an instance of OrderBean from a JSON string
order_bean_instance = OrderBean.from_json(json)
# print the JSON string representation of the object
print(OrderBean.to_json())

# convert the object into a dict
order_bean_dict = order_bean_instance.to_dict()
# create an instance of OrderBean from a dict
order_bean_from_dict = OrderBean.from_dict(order_bean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


