# GetNewOrdersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**Status**](Status.md) |  | [optional] 
**data** | [**GetNewOrdersBean**](GetNewOrdersBean.md) |  | [optional] 

## Example

```python
from order_api_client.models.get_new_orders_response import GetNewOrdersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetNewOrdersResponse from a JSON string
get_new_orders_response_instance = GetNewOrdersResponse.from_json(json)
# print the JSON string representation of the object
print(GetNewOrdersResponse.to_json())

# convert the object into a dict
get_new_orders_response_dict = get_new_orders_response_instance.to_dict()
# create an instance of GetNewOrdersResponse from a dict
get_new_orders_response_from_dict = GetNewOrdersResponse.from_dict(get_new_orders_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


