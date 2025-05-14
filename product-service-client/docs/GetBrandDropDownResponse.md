# GetBrandDropDownResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**Status**](Status.md) |  | [optional] 
**data** | [**BrandDropDownBean**](BrandDropDownBean.md) |  | [optional] 

## Example

```python
from product_api_client.models.get_brand_drop_down_response import GetBrandDropDownResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBrandDropDownResponse from a JSON string
get_brand_drop_down_response_instance = GetBrandDropDownResponse.from_json(json)
# print the JSON string representation of the object
print(GetBrandDropDownResponse.to_json())

# convert the object into a dict
get_brand_drop_down_response_dict = get_brand_drop_down_response_instance.to_dict()
# create an instance of GetBrandDropDownResponse from a dict
get_brand_drop_down_response_from_dict = GetBrandDropDownResponse.from_dict(get_brand_drop_down_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


