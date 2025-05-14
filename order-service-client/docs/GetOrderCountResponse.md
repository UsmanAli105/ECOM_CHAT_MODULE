# GetOrderCountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**Status**](Status.md) |  | [optional] 
**data** | [**OrderCountBean**](OrderCountBean.md) |  | [optional] 

## Example

```python
from order_api_client.models.get_order_count_response import GetOrderCountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrderCountResponse from a JSON string
get_order_count_response_instance = GetOrderCountResponse.from_json(json)
# print the JSON string representation of the object
print(GetOrderCountResponse.to_json())

# convert the object into a dict
get_order_count_response_dict = get_order_count_response_instance.to_dict()
# create an instance of GetOrderCountResponse from a dict
get_order_count_response_from_dict = GetOrderCountResponse.from_dict(get_order_count_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


