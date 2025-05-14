# GetNewOrdersBean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_orders** | [**List[NewOrderBean]**](NewOrderBean.md) |  | [optional] 

## Example

```python
from order_api_client.models.get_new_orders_bean import GetNewOrdersBean

# TODO update the JSON string below
json = "{}"
# create an instance of GetNewOrdersBean from a JSON string
get_new_orders_bean_instance = GetNewOrdersBean.from_json(json)
# print the JSON string representation of the object
print(GetNewOrdersBean.to_json())

# convert the object into a dict
get_new_orders_bean_dict = get_new_orders_bean_instance.to_dict()
# create an instance of GetNewOrdersBean from a dict
get_new_orders_bean_from_dict = GetNewOrdersBean.from_dict(get_new_orders_bean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


