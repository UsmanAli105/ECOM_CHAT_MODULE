# OrderCountBean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from order_api_client.models.order_count_bean import OrderCountBean

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCountBean from a JSON string
order_count_bean_instance = OrderCountBean.from_json(json)
# print the JSON string representation of the object
print(OrderCountBean.to_json())

# convert the object into a dict
order_count_bean_dict = order_count_bean_instance.to_dict()
# create an instance of OrderCountBean from a dict
order_count_bean_from_dict = OrderCountBean.from_dict(order_count_bean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


