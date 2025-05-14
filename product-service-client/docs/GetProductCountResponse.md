# GetProductCountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**Status**](Status.md) |  | [optional] 
**data** | [**ProductCountBean**](ProductCountBean.md) |  | [optional] 

## Example

```python
from product_api_client.models.get_product_count_response import GetProductCountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetProductCountResponse from a JSON string
get_product_count_response_instance = GetProductCountResponse.from_json(json)
# print the JSON string representation of the object
print(GetProductCountResponse.to_json())

# convert the object into a dict
get_product_count_response_dict = get_product_count_response_instance.to_dict()
# create an instance of GetProductCountResponse from a dict
get_product_count_response_from_dict = GetProductCountResponse.from_dict(get_product_count_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


